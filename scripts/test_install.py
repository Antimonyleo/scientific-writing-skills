#!/usr/bin/env python3
"""Exercise installation preservation and refusal behavior in temporary fixtures."""

import tempfile
import unittest
from pathlib import Path

from install import content_map, install


class InstallChecks(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.target = Path(self.workspace.name) / "host-skills"
        self.root = Path(__file__).resolve().parents[1]

    def test_copy_idempotence_and_backup(self):
        install(self.root, self.target)
        for source in (self.root / "skills").iterdir():
            self.assertEqual(content_map(source), content_map(self.target / source.name))
        first_state = content_map(self.target)
        install(self.root, self.target)
        self.assertEqual(content_map(self.target), first_state)
        self.assertFalse(list(self.target.glob(".scientific-writing-backup-*")))
        changed = self.target / "academic-writing" / "SKILL.md"
        changed.write_text("Personal version\n")
        install(self.root, self.target)
        backups = list(self.target.glob(".scientific-writing-backup-*"))
        self.assertEqual(len(backups), 1)
        self.assertEqual((backups[0] / "academic-writing" / "SKILL.md").read_text(), "Personal version\n")
        self.assertEqual(content_map(self.target / "academic-writing"), content_map(self.root / "skills/academic-writing"))

    def test_symlink_rejected_before_any_install(self):
        self.target.mkdir()
        external = Path(self.workspace.name) / "owned-elsewhere"
        external.mkdir()
        (self.target / "research-ideation").symlink_to(external, target_is_directory=True)
        with self.assertRaises(ValueError):
            install(self.root, self.target)
        self.assertFalse((self.target / "academic-writing").exists())
        self.assertEqual(list(external.iterdir()), [])

    def test_nested_symlink_rejected(self):
        install(self.root, self.target)
        link = self.target / "research-ideation" / "external"
        link.symlink_to(self.root / "README.md")
        before = (self.target / "academic-writing/SKILL.md").read_bytes()
        with self.assertRaises(ValueError):
            install(self.root, self.target)
        self.assertTrue(link.is_symlink())
        self.assertEqual((self.target / "academic-writing/SKILL.md").read_bytes(), before)

    def test_repository_overlap_rejected(self):
        with self.assertRaises(ValueError):
            install(self.root, self.root / "skills")


if __name__ == "__main__":
    unittest.main()
