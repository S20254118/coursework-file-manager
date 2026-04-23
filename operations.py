from abc import ABC, abstractmethod


class FileOperation(ABC):
    def __init__(self, file_manager):
        self._file_manager = file_manager

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class CreateFileOperation(FileOperation):
    def __init__(self, file_manager, filename):
        super().__init__(file_manager)
        self._filename = filename

    def execute(self):
        self._file_manager.create_file(self._filename)

    def undo(self):
        self._file_manager.delete_file(self._filename)


class DeleteFileOperation(FileOperation):
    def __init__(self, file_manager, filename):
        super().__init__(file_manager)
        self._filename = filename
        self._backup_content = ""

    def execute(self):
        self._backup_content = self._file_manager.read_file(self._filename)
        self._file_manager.delete_file(self._filename)

    def undo(self):
        self._file_manager.create_file(self._filename)
        self._file_manager.write_file(self._filename, self._backup_content)


class RenameFileOperation(FileOperation):
    def __init__(self, file_manager, old_name, new_name):
        super().__init__(file_manager)
        self._old_name = old_name
        self._new_name = new_name

    def execute(self):
        self._file_manager.rename_file(self._old_name, self._new_name)

    def undo(self):
        self._file_manager.rename_file(self._new_name, self._old_name)


class WriteFileOperation(FileOperation):
    def __init__(self, file_manager, filename, new_content):
        super().__init__(file_manager)
        self._filename = filename
        self._new_content = new_content
        self._old_content = ""

    def execute(self):
        self._old_content = self._file_manager.read_file(self._filename)
        self._file_manager.write_file(self._filename, self._new_content)

    def undo(self):
        self._file_manager.write_file(self._filename, self._old_content)