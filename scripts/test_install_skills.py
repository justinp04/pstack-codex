"""Exercise installation safety using a small real filesystem bundle."""

import contextlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import install_skills


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'bundle'
        self.destination = Path(self.temp.name) / 'installed'
        for name in ('pstack', 'how'):
            folder = self.root / 'skills' / name
            folder.mkdir(parents=True)
            (folder / 'SKILL.md').write_text(f'name: {name}\n')
        self.registry = {'core': 'pstack', 'entries': [{'skill': 'how'}]}
        self.write_registry()
        root_patch = patch.object(install_skills, 'ROOT', self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)

    def write_registry(self):
        (self.root / 'entrypoints.json').write_text(json.dumps(self.registry))

    def install(self):
        with contextlib.redirect_stdout(io.StringIO()):
            install_skills.install(self.destination)

    def test_install_and_identical_reinstall(self):
        self.install()
        before = install_skills.manifest(self.destination)
        self.install()
        self.assertEqual(before, install_skills.manifest(self.destination))
        self.assertEqual({'pstack', 'how'}, {p.name for p in self.destination.iterdir()})

    def test_conflict_preserves_existing_and_installs_nothing(self):
        existing = self.destination / 'how'
        existing.mkdir(parents=True)
        (existing / 'SKILL.md').write_text('unrelated skill')
        before = install_skills.manifest(self.destination)
        with self.assertRaises(FileExistsError):
            self.install()
        self.assertEqual(before, install_skills.manifest(self.destination))
        self.assertFalse((self.destination / 'pstack').exists())

    def test_path_traversal_refused_before_writes(self):
        self.registry['entries'][0]['skill'] = '../outside'
        self.write_registry()
        with self.assertRaises(ValueError):
            self.install()
        self.assertFalse(self.destination.exists())

    def test_source_symlink_refused_before_writes(self):
        (self.root / 'skills/how/link').symlink_to(self.root / 'entrypoints.json')
        with self.assertRaises(ValueError):
            self.install()
        self.assertFalse(self.destination.exists())

    def test_failed_second_move_rolls_back_new_skills(self):
        real_rename = os.rename
        calls = 0

        def fail_second(source, destination):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError('simulated filesystem failure')
            return real_rename(source, destination)

        with patch.object(install_skills.os, 'rename', side_effect=fail_second):
            with self.assertRaises(OSError):
                self.install()
        self.assertEqual([], list(self.destination.iterdir()))


if __name__ == '__main__':
    unittest.main()
