import shutil
import unittest
from pathlib import Path

from file_manager import FileManager
from history import OperationHistory
from operations import (
    CreateFileOperation,
    DeleteFileOperation,
    RenameFileOperation,
    WriteFileOperation,
)


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_workspace"
        self.manager = FileManager(self.test_dir)

    def tearDown(self):
        path = Path(self.test_dir)
        if path.exists():
            shutil.rmtree(path)

    def test_create_file(self):
        self.manager.create_file("test.txt")
        self.assertIn("test.txt", self.manager.list_files())

    def test_write_and_read_file(self):
        self.manager.create_file("test.txt")
        self.manager.write_file("test.txt", "Hello")
        content = self.manager.read_file("test.txt")
        self.assertEqual(content, "Hello")

    def test_delete_file(self):
        self.manager.create_file("test.txt")
        self.manager.delete_file("test.txt")
        self.assertNotIn("test.txt", self.manager.list_files())

    def test_rename_file(self):
        self.manager.create_file("old.txt")
        self.manager.rename_file("old.txt", "new.txt")
        self.assertIn("new.txt", self.manager.list_files())
        self.assertNotIn("old.txt", self.manager.list_files())


class TestOperationHistory(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_workspace_history"
        self.manager = FileManager(self.test_dir)
        self.history = OperationHistory()

    def tearDown(self):
        path = Path(self.test_dir)
        if path.exists():
            shutil.rmtree(path)

    def test_create_operation_undo_redo(self):
        operation = CreateFileOperation(self.manager, "file.txt")

        self.history.execute_operation(operation)
        self.assertIn("file.txt", self.manager.list_files())

        self.history.undo()
        self.assertNotIn("file.txt", self.manager.list_files())

        self.history.redo()
        self.assertIn("file.txt", self.manager.list_files())

    def test_write_operation_undo(self):
        self.manager.create_file("file.txt")
        self.manager.write_file("file.txt", "Old text")

        operation = WriteFileOperation(self.manager, "file.txt", "New text")
        self.history.execute_operation(operation)
        self.assertEqual(self.manager.read_file("file.txt"), "New text")

        self.history.undo()
        self.assertEqual(self.manager.read_file("file.txt"), "Old text")

    def test_delete_operation_undo(self):
        self.manager.create_file("file.txt")
        self.manager.write_file("file.txt", "Text")

        operation = DeleteFileOperation(self.manager, "file.txt")
        self.history.execute_operation(operation)
        self.assertNotIn("file.txt", self.manager.list_files())

        self.history.undo()
        self.assertIn("file.txt", self.manager.list_files())
        self.assertEqual(self.manager.read_file("file.txt"), "Text")

    def test_rename_operation_undo(self):
        self.manager.create_file("old.txt")

        operation = RenameFileOperation(self.manager, "old.txt", "new.txt")
        self.history.execute_operation(operation)
        self.assertIn("new.txt", self.manager.list_files())

        self.history.undo()
        self.assertIn("old.txt", self.manager.list_files())


if __name__ == "__main__":
    unittest.main()
