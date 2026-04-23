from file_manager import FileManager
from history import OperationHistory
from operations import (
    CreateFileOperation,
    DeleteFileOperation,
    RenameFileOperation,
    WriteFileOperation
)


def main():
    manager = FileManager()
    history = OperationHistory()

    while True:
        print("\n--- File Manager ---")
        print("1. Create file")
        print("2. Write to file")
        print("3. Read file")
        print("4. Rename file")
        print("5. Delete file")
        print("6. List files")
        print("7. Undo")
        print("8. Redo")
        print("9. Exit")

        choice = input("Choose: ")

        try:
            if choice == "1":
                name = input("File name: ")
                history.execute_operation(CreateFileOperation(manager, name))

            elif choice == "2":
                name = input("File name: ")
                text = input("Text: ")
                history.execute_operation(WriteFileOperation(manager, name, text))

            elif choice == "3":
                name = input("File name: ")
                print(manager.read_file(name))

            elif choice == "4":
                old = input("Old name: ")
                new = input("New name: ")
                history.execute_operation(RenameFileOperation(manager, old, new))

            elif choice == "5":
                name = input("File name: ")
                history.execute_operation(DeleteFileOperation(manager, name))

            elif choice == "6":
                print(manager.list_files())

            elif choice == "7":
                history.undo()

            elif choice == "8":
                history.redo()

            elif choice == "9":
                break

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()