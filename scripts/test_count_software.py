"""Regression tests for label parsing and safe README updates."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SPEC = importlib.util.spec_from_file_location('software_counter', Path(__file__).with_name('count-software.py'))
COUNTER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = COUNTER
SPEC.loader.exec_module(COUNTER)


class CountTests(unittest.TestCase):
    def test_only_explicit_standalone_comments_count(self):
        self.assertEqual(COUNTER.parse_count('<!-- software-count: 1 -->\n# App'), 1)
        self.assertEqual(COUNTER.parse_count('\ufeff<!-- software-count: 0 -->'), 0)
        for text in ('# <img src="app.png"> App', 'software-count: 9',
                     '`<!-- software-count: 9 -->`', 'Text <!-- software-count: 9 -->'):
            with self.subTest(text=text):
                self.assertIsNone(COUNTER.parse_count(text))

    def test_fenced_examples_are_ignored(self):
        examples = ('```markdown\n<!-- software-count: 99 -->\n```\n',
                    '~~~~\n<!-- software-count: 99 -->\n~~~\n')
        for text in examples:
            with self.subTest(text=text):
                self.assertIsNone(COUNTER.parse_count(text))
        self.assertEqual(COUNTER.parse_count(examples[0] + '<!-- software-count: 2 -->'), 2)

    def test_indented_code_examples_are_ignored(self):
        for prefix in ('    ', '\t', '  \t'):
            with self.subTest(prefix=prefix):
                self.assertIsNone(COUNTER.parse_count(prefix + '<!-- software-count: 99 -->'))
        self.assertEqual(COUNTER.parse_count('   <!-- software-count: 1 -->'), 1)

    def test_invalid_and_duplicate_tags_fail(self):
        for text in ('<!-- software-count: -1 -->', '<!-- software-count: one -->',
                     '<!-- software-count: 1 -->\n<!-- software-count: 1 -->'):
            with self.subTest(text=text), self.assertRaises(COUNTER.CounterError):
                COUNTER.parse_count(text)

    def test_header_line_limit(self):
        self.assertEqual(COUNTER.parse_count('\n' * 19 + '<!-- software-count: 2 -->'), 2)
        self.assertIsNone(COUNTER.parse_count('\n' * 20 + '<!-- software-count: 2 -->'))


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='software-counter-test-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.category = self.root / 'Windows' / 'Optional'
        self.category.mkdir(parents=True)

    def document(self, name='app.md', text='<!-- software-count: 2 -->\n# App\n'):
        path = self.category / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode('utf-8'))
        return path

    def readmes(self):
        for name in ('README_zh.md', 'README_en.md'):
            (self.root / name).write_bytes(
                ('# Original title\n\n' + COUNTER.STATS_START + '\nold table\n'
                 + COUNTER.STATS_END + '\n\nOriginal footer').encode('utf-8'))

    def run_counter(self, *arguments):
        with contextlib.redirect_stdout(io.StringIO()) as stdout, contextlib.redirect_stderr(io.StringIO()) as stderr:
            code = COUNTER.main(list(arguments), root=self.root)
        return code, stdout.getvalue(), stderr.getvalue()

    def test_directory_exclusions_are_exact_and_pruned(self):
        self.document()
        self.document('config.md', '<!-- software-count: 0 -->\n')
        self.document('latest-app/app.md', '<!-- software-count: 1 -->\n')
        self.document('README.MD', 'invalid metadata should be ignored')
        pruned_names = []

        def fake_walk(directory, **kwargs):
            names = ['.obsidian', '.git', 'test', 'latest-app']
            yield str(directory), names, ['app.md', 'config.md', 'README.MD']
            pruned_names.extend(names)
            if '.obsidian' in names or 'test' in names:
                self.fail('Excluded directories were not pruned')
            yield str(directory / 'latest-app'), [], ['app.md']

        with mock.patch.object(COUNTER.os, 'walk', side_effect=fake_walk):
            entries = COUNTER.scan(self.root)
        self.assertEqual(pruned_names, ['latest-app'])
        self.assertEqual(sorted(entry.count for entry in entries), [0, 1, 2])

    def test_invalid_utf8_fails_instead_of_defaulting_to_one(self):
        self.document().write_bytes(b'\xff')
        with self.assertRaises(COUNTER.CounterError):
            COUNTER.scan(self.root)

    def test_missing_file_is_an_error(self):
        with self.assertRaises(COUNTER.CounterError):
            COUNTER.read_utf8(self.root / 'missing.md')

    def test_missing_tags_are_not_inferred_and_block_writes(self):
        self.document(text='# <img src="app.png"> App\n')
        self.readmes()
        originals = {path: path.read_bytes() for path in self.root.glob('README_*.md')}
        self.assertEqual(self.run_counter('--dry-run')[0], 0)
        self.assertEqual(self.run_counter('--check')[0], 1)
        self.assertEqual(self.run_counter()[0], 2)
        for path, original in originals.items():
            self.assertEqual(path.read_bytes(), original)

    def test_preview_does_not_require_readmes(self):
        self.document()
        code, stdout, stderr = self.run_counter('--dry-run', '--details')
        self.assertEqual(code, 0)
        self.assertIn('[2] Windows/Optional/app.md', stdout)
        self.assertEqual(stderr, '')
        self.assertEqual(list(self.root.glob('README_*.md')), [])

    def test_readme_encoding_newlines_and_endings_are_preserved(self):
        path = self.root / 'README_zh.md'
        for bom in (b'', b'\xef\xbb\xbf'):
            for newline in ('\n', '\r\n'):
                for trailing in ('', newline):
                    with self.subTest(bom=bom, newline=newline, trailing=trailing):
                        prefix = '# Title' + newline + COUNTER.STATS_START
                        suffix = COUNTER.STATS_END + newline + 'Footer' + trailing
                        original = bom + (prefix + newline + 'old' + newline + suffix).encode('utf-8')
                        path.write_bytes(original)
                        update = COUNTER.prepare_update(path, '| new |\n| table |')
                        expected = bom + (prefix + newline + '| new |' + newline
                                          + '| table |' + newline + suffix).encode('utf-8')
                        self.assertEqual(update.replacement, expected)

    def test_missing_duplicate_and_reversed_markers_fail(self):
        path = self.root / 'README_zh.md'
        examples = ('no markers', COUNTER.STATS_START + '\n' + COUNTER.STATS_START + '\n' + COUNTER.STATS_END,
                    COUNTER.STATS_END + '\n' + COUNTER.STATS_START)
        for text in examples:
            with self.subTest(text=text):
                path.write_bytes(text.encode('utf-8'))
                with self.assertRaises(COUNTER.CounterError):
                    COUNTER.prepare_update(path, 'new table')

    def test_both_readmes_are_validated_before_writing(self):
        self.document()
        self.readmes()
        chinese = self.root / 'README_zh.md'
        original = chinese.read_bytes()
        (self.root / 'README_en.md').write_bytes(b'no markers')
        self.assertEqual(self.run_counter()[0], 2)
        self.assertEqual(chinese.read_bytes(), original)

    def test_check_and_repeated_updates_do_not_write(self):
        self.document()
        self.readmes()
        self.assertEqual(self.run_counter('--check')[0], 1)
        self.assertEqual(self.run_counter()[0], 0)
        paths = list(self.root.glob('README_*.md'))
        snapshots = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in paths}
        self.assertEqual(self.run_counter('--check')[0], 0)
        code, stdout, _ = self.run_counter()
        self.assertEqual(code, 0)
        self.assertIn('未写入文件', stdout)
        for path, snapshot in snapshots.items():
            self.assertEqual((path.read_bytes(), path.stat().st_mtime_ns), snapshot)

    def test_partial_commit_failure_restores_originals(self):
        self.readmes()
        paths = list(self.root.glob('README_*.md'))
        originals = {path: path.read_bytes() for path in paths}
        updates = [COUNTER.prepare_update(path, 'new table') for path in paths]
        real_replace = os.replace
        calls = 0

        def fail_second_replace(source, target):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError('simulated second-file failure')
            return real_replace(source, target)

        with mock.patch.object(COUNTER.os, 'replace', side_effect=fail_second_replace):
            with self.assertRaises(COUNTER.CounterError):
                COUNTER.commit_updates(updates)
        for path, original in originals.items():
            self.assertEqual(path.read_bytes(), original)
        self.assertEqual(list(self.root.glob('*.tmp')), [])

    def test_concurrent_changes_are_not_overwritten(self):
        self.readmes()
        path = self.root / 'README_zh.md'
        update = COUNTER.prepare_update(path, 'new table')
        path.write_bytes(b'concurrent user edit')
        with self.assertRaises(COUNTER.CounterError):
            COUNTER.commit_updates([update])
        self.assertEqual(path.read_bytes(), b'concurrent user edit')


if __name__ == '__main__':
    unittest.main()
