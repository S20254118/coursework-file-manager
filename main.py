from file_manager import FileManager
from history import OperationHistory
from operations import (
    CreateFileOperation,
    DeleteFileOperation,
    RenameFileOperation,
    WriteFileOperation,
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
                operation = CreateFileOperation(manager, name)
                history.execute_operation(operation)

            elif choice == "2":
                name = input("File name: ")
                text = input("Text: ")
                operation = WriteFileOperation(manager, name, text)
                history.execute_operation(operation)

            elif choice == "3":
                name = input("File name: ")
                print(manager.read_file(name))

            elif choice == "4":
                old_name = input("Old name: ")
                new_name = input("New name: ")
                operation = RenameFileOperation(manager, old_name, new_name)
                history.execute_operation(operation)

            elif choice == "5":
                name = input("File name: ")
                operation = DeleteFileOperation(manager, name)
                history.execute_operation(operation)

            elif choice == "6":
                files = manager.list_files()
                if files:
                    for file in files:
                        print(file)
                else:
                    print("No files found.")

            elif choice == "7":
                history.undo()

            elif choice == "8":
                history.redo()

            elif choice == "9":
                print("Program closed.")
                break

            else:
                print("Invalid choice.")

        except Exception as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
