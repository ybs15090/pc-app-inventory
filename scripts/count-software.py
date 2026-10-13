#!/usr/bin/env python3
"""Count explicit software-count comments and maintain the two README tables."""

from __future__ import annotations

import argparse
import os
import re
import stat
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

PLATFORMS = ('Windows', 'Linux', 'MacOS', 'General', 'Android', 'iOS')
CATEGORIES = ('Essential', 'Optional')
EXCLUDED_NAMES = {'readme.md', 'claude.md', 'agents.md', 'test.md'}
EXCLUDED_DIRS = {'.obsidian', '.git', 'test', '__pycache__'}
HEADER_LINES = 20
COUNT_TAG = re.compile(r'^ {0,3}<!--\s*software-count:\s*([0-9]+)\s*-->\s*$')
COUNT_PREFIX = re.compile(r'^ {0,3}<!--\s*software-count\b')
FENCE = re.compile(r'^ {0,3}(`{3,}|~{3,})(.*)$')
STATS_START = '<!-- software-stats:start -->'
STATS_END = '<!-- software-stats:end -->'


class CounterError(Exception):
    """A validation or file operation failed; the update must not proceed."""


@dataclass(frozen=True)
class Entry:
    path: Path
    platform: str
    category: str
    count: Optional[int]


@dataclass(frozen=True)
class Update:
    path: Path
    original: bytes
    replacement: bytes


def parse_count(text: str, source: str = '<document>') -> Optional[int]:
    """Read one standalone count comment in the first 20 lines, outside fences."""
    found = []
    fence_char = None
    fence_length = 0
    for number, line in enumerate(text.lstrip('\ufeff').splitlines()[:HEADER_LINES], 1):
        fence = FENCE.match(line)
        if fence:
            marker, tail = fence.groups()
            if fence_char is None:
                fence_char, fence_length = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_length and not tail.strip():
                fence_char = None
            continue
        if fence_char is not None:
            continue
        tag = COUNT_TAG.fullmatch(line)
        if tag:
            found.append((number, int(tag.group(1))))
        elif COUNT_PREFIX.match(line):
            raise CounterError(f'{source}:{number}: software-count 必须是非负整数的独立 HTML 注释')
    if len(found) > 1:
        raise CounterError(f'{source}: 前 {HEADER_LINES} 行存在重复 software-count 标签')
    return found[0][1] if found else None


def read_utf8(path: Path) -> Tuple[bytes, str]:
    try:
        raw = path.read_bytes()
        return raw, raw.decode('utf-8-sig')
    except (OSError, UnicodeError) as exc:
        raise CounterError(f'无法读取 UTF-8 文件 {path}: {exc}') from exc


def scan(root: Path) -> List[Entry]:
    entries = []

    def walk_error(error: OSError) -> None:
        raise CounterError(f'无法枚举目录: {error}') from error

    for platform in PLATFORMS:
        for category in CATEGORIES:
            directory = root / platform / category
            if not directory.exists():
                continue
            if not directory.is_dir():
                raise CounterError(f'预期为目录: {directory}')
            for current, directories, files in os.walk(directory, followlinks=False, onerror=walk_error):
                directories[:] = sorted(
                    name for name in directories
                    if name.casefold() not in EXCLUDED_DIRS
                    and not (Path(current) / name).is_symlink()
                )
                for name in sorted(files):
                    path = Path(current) / name
                    if path.suffix.casefold() != '.md' or name.casefold() in EXCLUDED_NAMES:
                        continue
                    if path.is_symlink():
                        continue
                    _, text = read_utf8(path)
                    value = parse_count(text, path.relative_to(root).as_posix())
                    entries.append(Entry(path, platform, category, value))
    return entries


def totals(entries: Sequence[Entry]) -> List[Tuple[str, int, int, int]]:
    rows = []
    for platform in PLATFORMS:
        values = [sum(entry.count or 0 for entry in entries
                      if entry.platform == platform and entry.category == category)
                  for category in CATEGORIES]
        rows.append((platform, values[0], values[1], sum(values)))
    return rows


def make_table(rows: Sequence[Tuple[str, int, int, int]], english: bool = False) -> str:
    headers = ('Platform', 'Essential', 'Optional', 'Total') if english else ('平台', 'Essential', 'Optional', '合计')
    lines = ['| ' + ' | '.join(headers) + ' |', '| --- | --- | --- | --- |']
    lines.extend(f'| {platform} | {essential} | {optional} | **{total}** |'
                 for platform, essential, optional, total in rows)
    return '\n'.join(lines)


def prepare_update(path: Path, table: str) -> Update:
    original, text = read_utf8(path)
    markers = []
    for marker in (STATS_START, STATS_END):
        matches = list(re.finditer(r'(?m)^[ \t]*' + re.escape(marker) + r'[ \t]*\r?$', text))
        if len(matches) != 1:
            raise CounterError(f'{path.name}: 必须且只能有一处 {marker}')
        markers.append(matches[0])
    start, end = markers
    if start.end() >= end.start():
        raise CounterError(f'{path.name}: 统计区块标记顺序错误')
    newline_match = re.search(r'\r\n|\n|\r', text)
    newline = newline_match.group() if newline_match else '\n'
    start_position = start.end() - (1 if start.group().endswith('\r') else 0)
    replacement_text = (text[:start_position] + newline + table.replace('\n', newline)
                        + newline + text[end.start():])
    bom = b'\xef\xbb\xbf' if original.startswith(b'\xef\xbb\xbf') else b''
    return Update(path, original, bom + replacement_text.encode('utf-8'))


def stage_bytes(path: Path, data: bytes) -> Path:
    descriptor, name = tempfile.mkstemp(prefix='.' + path.name + '.', suffix='.tmp', dir=str(path.parent))
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, 'wb') as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(str(temporary), stat.S_IMODE(path.stat().st_mode))
    except BaseException:
        temporary.unlink()
        raise
    return temporary


def commit_updates(updates: Sequence[Update]) -> int:
    changed = [update for update in updates if update.original != update.replacement]
    staged = []
    committed = []
    retained = set()
    try:
        for update in changed:
            if update.path.read_bytes() != update.original:
                raise CounterError(f'{update.path.name}: 文件在校验后发生变化，请重新运行')
            backup = stage_bytes(update.path, update.original)
            staged.append((update, backup, None))
            replacement = stage_bytes(update.path, update.replacement)
            staged[-1] = (update, backup, replacement)
        for update, backup, replacement in staged:
            if update.path.read_bytes() != update.original:
                raise CounterError(f'{update.path.name}: 文件在校验后发生变化，请重新运行')
            os.replace(str(replacement), str(update.path))
            committed.append((update, backup))
    except BaseException as exc:
        rollback_errors = []
        for update, backup in reversed(committed):
            try:
                os.replace(str(backup), str(update.path))
            except OSError as rollback_error:
                retained.add(backup)
                rollback_errors.append(f'{update.path.name} 回退失败，原文件保留在 {backup}: {rollback_error}')
        if isinstance(exc, KeyboardInterrupt) and not rollback_errors:
            raise
        detail = '; '.join([str(exc)] + rollback_errors)
        raise CounterError(f'更新失败: {detail}') from exc
    finally:
        for _, backup, replacement in staged:
            for temporary in (backup, replacement):
                if temporary is not None and temporary not in retained:
                    try:
                        temporary.unlink(missing_ok=True)
                    except OSError as cleanup_error:
                        print(f'警告：临时文件未能清理 {temporary}: {cleanup_error}', file=sys.stderr)
    return len(changed)


def main(argv: Optional[Sequence[str]] = None, root: Optional[Path] = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    if sys.version_info < (3, 8):
        print('错误：需要 Python 3.8 或更新版本', file=sys.stderr)
        return 2
    parser = argparse.ArgumentParser(description='仅按软件文档的 software-count 标签统计；默认更新中英文 README。')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--dry-run', action='store_true', help='只显示统计，不读取或写入 README')
    mode.add_argument('--check', action='store_true', help='检查标签和 README；需要更新时退出码为 1')
    mode.add_argument('--write', action='store_true', help='更新 README（默认行为）')
    parser.add_argument('--details', action='store_true', help='显示每份文档的标签计数和缺失标签')
    args = parser.parse_args(argv)
    root = (root or Path(__file__).resolve().parent.parent).resolve()
    try:
        entries = scan(root)
        rows = totals(entries)
        print('## 软件收录统计\n')
        print(make_table(rows))
        print(f'\n按标签合计：{sum(row[3] for row in rows)} 项\n')
        if args.details:
            print('逐文件计数：')
            for entry in entries:
                label = str(entry.count) if entry.count is not None else '缺失'
                print(f'  [{label}] {entry.path.relative_to(root).as_posix()}')
            print()
        missing = [entry for entry in entries if entry.count is None]
        if missing:
            print(f'发现 {len(missing)} 份正文缺少前 {HEADER_LINES} 行内的 software-count 标签：', file=sys.stderr)
            for entry in missing:
                print('  ' + entry.path.relative_to(root).as_posix(), file=sys.stderr)
            print('缺失标签的文件未计入；软件填 1，合集填实际数量，配置或非软件专题填 0。', file=sys.stderr)
        if args.dry_run:
            print('预览完成，未修改文件。')
            return 0
        if missing:
            print('检查未通过，未修改 README。', file=sys.stderr)
            return 1 if args.check else 2
        updates = [prepare_update(root / 'README_zh.md', make_table(rows)),
                   prepare_update(root / 'README_en.md', make_table(rows, english=True))]
        changed = [update.path.name for update in updates if update.original != update.replacement]
        if args.check:
            if changed:
                print('统计表需要更新：' + '、'.join(changed))
                return 1
            print('检查通过：标签完整，中英文统计表已是最新。')
            return 0
        count = commit_updates(updates)
        print(f'已更新 {count} 份 README 统计表。' if count else '统计表已是最新，未写入文件。')
        return 0
    except CounterError as exc:
        print(f'错误：{exc}', file=sys.stderr)
        return 2
    except OSError as exc:
        print(f'错误：文件操作失败: {exc}', file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print('操作已取消。', file=sys.stderr)
        return 130


if __name__ == '__main__':
    raise SystemExit(main())
