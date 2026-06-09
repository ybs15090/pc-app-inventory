#!/usr/bin/env python3
# 统计仓库中各平台收录的软件数量，并自动更新 README_zh.md 和 README_en.md
# 用法: python scripts/count-software.py
#
# 计数规则（按优先级）：
#   1. <!-- software-count: N -->  手动指定（最高优先级）
#   2. 统计 ## <img 标题的数量       多软件文件中带图标的二级标题
#   3. 统计 # <img 标题的数量        单/多软件文件带图标的一级标题
#   4. 兜底 → 1                     无图标标记但视为 1 款
# 排除: README.md, CLAUDE.md, test.md, config.md

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

EXCLUDED_NAMES = {'README.md', 'CLAUDE.md', 'test.md', 'config.md'}
PLATFORMS = ['Windows', 'Linux', 'MacOS', 'General', 'Android', 'iOS']


def count_in_file(path: Path) -> int:
    try:
        lines = path.read_text(encoding='utf-8', errors='ignore').splitlines()
    except OSError:
        return 1

    for line in lines[:20]:
        m = re.search(r'software-count:\s*(\d+)', line)
        if m:
            return int(m.group(1))

    h2 = sum(1 for l in lines if l.startswith('## <img'))
    if h2 > 0:
        return h2

    h1 = sum(1 for l in lines if l.startswith('# <img'))
    if h1 > 0:
        return h1

    return 1


def count_software(directory: Path) -> int:
    if not directory.is_dir():
        return 0
    total = 0
    for md in directory.rglob('*.md'):
        if md.name in EXCLUDED_NAMES:
            continue
        if 'test' in md.parts:
            continue
        total += count_in_file(md)
    return total


def update_table(readme: Path, header: str, new_table: str) -> None:
    if not readme.exists():
        print(f'警告：{readme} 不存在，跳过')
        return

    lines = readme.read_text(encoding='utf-8').splitlines(keepends=True)
    result = []
    i = 0
    replaced = False
    while i < len(lines):
        if not replaced and header in lines[i]:
            result.append(new_table + '\n')
            i += 1
            while i < len(lines) and lines[i].startswith('|'):
                i += 1
            replaced = True
        else:
            result.append(lines[i])
            i += 1
    readme.write_text(''.join(result), encoding='utf-8')


def make_table(headers: list[str], sep: list[str], rows: list[tuple]) -> str:
    lines = [
        '| ' + ' | '.join(headers) + ' |',
        '| ' + ' | '.join(sep) + ' |',
    ]
    for platform, ess, opt, total in rows:
        lines.append(f'| {platform} | {ess} | {opt} | **{total}** |')
    return '\n'.join(lines)


def main() -> None:
    root = Path(__file__).parent.parent

    rows = []
    grand_total = 0
    for platform in PLATFORMS:
        ess = count_software(root / platform / 'Essential')
        opt = count_software(root / platform / 'Optional')
        total = ess + opt
        rows.append((platform, ess, opt, total))
        grand_total += total

    print('## 软件收录统计\n')
    print('| 平台 | Essential | Optional | 合计 |')
    print('|------|-----------|----------|------|')
    for platform, ess, opt, total in rows:
        print(f'| {platform} | {ess} | {opt} | **{total}** |')
    print(f'\n总计：{grand_total} 款软件\n')

    zh_table = make_table(
        ['平台', 'Essential', 'Optional', '合计'],
        ['------', '-----------', '----------', '------'],
        rows,
    )
    en_table = make_table(
        ['Platform', 'Essential', 'Optional', 'Total'],
        ['----------', '-----------', '----------', '-------'],
        rows,
    )

    update_table(root / 'README_zh.md', '| 平台 | Essential | Optional | 合计 |', zh_table)
    update_table(root / 'README_en.md', '| Platform | Essential | Optional | Total |', en_table)

    print('✓ README_zh.md 和 README_en.md 已更新')


if __name__ == '__main__':
    main()
