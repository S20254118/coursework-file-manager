from pathlib import Path


class FileManager:
    def __init__(self, base_directory="workspace"):
        self._base_directory = Path(base_directory)
        self._base_directory.mkdir(exist_ok=True)

    def _get_path(self, filename):
        return self._base_directory / filename

    def create_file(self, filename):
        path = self._get_path(filename)
        if path.exists():
            raise FileExistsError(f"File '{filename}' already exists.")
        path.touch()

    def delete_file(self, filename):
        path = self._get_path(filename)
        if not path.exists():
            raise FileNotFoundError(f"File '{filename}' not found.")
        path.unlink()

    def rename_file(self, old_name, new_name):
        old_path = self._get_path(old_name)
        new_path = self._get_path(new_name)

        if not old_path.exists():
            raise FileNotFoundError(f"File '{old_name}' not found.")
        if new_path.exists():
            raise FileExistsError(f"File '{new_name}' already exists.")

        old_path.rename(new_path)

    def write_file(self, filename, content):
        path = self._get_path(filename)
        if not path.exists():
            raise FileNotFoundError(f"File '{filename}' not found.")
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

    def read_file(self, filename):
        path = self._get_path(filename)
        if not path.exists():
            raise FileNotFoundError(f"File '{filename}' not found.")
        with open(path, "r", encoding="utf-8") as file:
            return file.read()

    def list_files(self):
        return [file.name for file in self._base_directory.iterdir() if file.is_file()]