import shutil
import unittest
from pathlib import Path

from file_manager import FileManager


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.dir = "test_workspace"
        self.manager = FileManager(self.dir)

    def tearDown(self):
        if Path(self.dir).exists():
            shutil.rmtree(self.dir)

    def test_create(self):
        self.manager.create_file("a.txt")
        self.assertIn("a.txt", self.manager.list_files())

    def test_write_read(self):
        self.manager.create_file("a.txt")
        self.manager.write_file("a.txt", "hello")
        self.assertEqual(self.manager.read_file("a.txt"), "hello")

    def test_delete(self):
        self.manager.create_file("a.txt")
        self.manager.delete_file("a.txt")
        self.assertNotIn("a.txt", self.manager.list_files())


if __name__ == "__main__":
    unittest.main()