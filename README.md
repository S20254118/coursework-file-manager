# 📂 File Manager System (OOP Coursework)

This project is a **File Manager System** developed in Python using Object-Oriented Programming (OOP) principles.

The system allows users to perform file operations and includes **undo/redo functionality**, demonstrating practical software design concepts.

---

## 🚀 Features

* Create file
* Write to file
* Read file
* Rename file
* Delete file
* List files
* Undo / Redo operations
* Error handling

---

## ▶️ How to run

### Run the program:

```bash
python main.py
```

### Run tests:

```bash
python -m unittest discover -s tests
```

---

## 🧠 OOP Principles Used

### 🔹 Abstraction

An abstract base class defines the structure for all file operations.

```python
class FileOperation(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass
```

---

### 🔹 Inheritance

Specific operations inherit from the base class:

```python
class CreateFileOperation(FileOperation):
    def execute(self):
        self._file_manager.create_file(self._filename)
```

---

### 🔹 Polymorphism

All operations are executed through the same interface:

```python
operation.execute()
operation.undo()
```

Each operation behaves differently but is used the same way.

---

### 🔹 Encapsulation

Internal data is protected:

```python
self._base_directory
self._undo_stack
```

---

## 🏗️ Design Pattern

### Command Pattern

The **Command Pattern** is used to represent file operations as objects.

This allows:

* storing operations in history
* implementing undo/redo
* separating logic from execution

Example:

```python
history.execute_operation(operation)
history.undo()
```

---

## 🔗 Object Relationships (Composition)

The system uses composition:

```python
self._undo_stack = []
self._redo_stack = []
```

`OperationHistory` stores and manages operations.

---

## 📂 File Handling (I/O)

The program works with real files:

```python
with open(path, "w", encoding="utf-8") as file:
    file.write(content)
```

Supports:

* reading
* writing
* deleting
* renaming

---

## 🧪 Testing

Unit tests are implemented using `unittest`.

Test coverage:

* file creation
* read/write operations
* delete functionality
* basic system behavior

Example output:

```
Ran tests successfully
OK
```

---

## 📁 Project Structure

```
project/
│
├── main.py
├── file_manager.py
├── operations.py
├── history.py
├── report.md
├── README.md
├── .gitignore
└── tests/
    └── test_file_manager.py
```

---

## 🧩 Example Workflow

```
1 → Create file
2 → Write content
3 → Read content
7 → Undo
8 → Redo
```

---

## ⚠️ Error Handling

The system handles common errors:

* file not found
* file already exists
* invalid operations

Example:

```python
raise FileNotFoundError("File not found")
```

---

## 🏁 Conclusion

This project demonstrates how OOP principles can be applied in real applications.

Key achievements:

* clear architecture
* use of design patterns
* modular structure
* reliable file operations

The system is simple but scalable and can be extended in the future.

---

## 🔮 Possible Improvements

* GUI interface
* file search
* folder navigation
* logging system
* file copy/move functionality
