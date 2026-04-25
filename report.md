# Failų valdymo sistema (OOP kursinis darbas)

## Įvadas

Šio kursinio darbo tikslas – sukurti paprastą failų valdymo sistemą naudojant Python programavimo kalbą ir objektinio programavimo (OOP) principus.

Programa leidžia atlikti pagrindines failų operacijas: kurti, skaityti, rašyti, pervadinti ir trinti failus. Taip pat įgyvendintas undo/redo funkcionalumas, kuris leidžia atšaukti arba pakartoti veiksmus.

---

## Analizė (Body / Analysis)

### Programos struktūra

Projektas susideda iš kelių pagrindinių dalių:

* `main.py` – vartotojo sąsaja
* `file_manager.py` – darbas su failais
* `operations.py` – operacijų klasės
* `history.py` – undo/redo logika
* `tests/` – vienetiniai testai

---

### OOP principų taikymas

#### Abstrakcija

Naudojama abstrakti klasė `FileOperation`, kuri apibrėžia bendrą operacijų struktūrą.

```python
class FileOperation(ABC):
    def __init__(self, file_manager):
        self._file_manager = file_manager

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass
```

---

#### Paveldėjimas

Konkrečios operacijos paveldi bazinę klasę.

```python
class CreateFileOperation(FileOperation):
    def execute(self):
        self._file_manager.create_file(self._filename)
```

---

#### Polimorfizmas

Visos operacijos vykdomos vienodu būdu:

```python
history.execute_operation(operation)
history.undo()
```

Skirtingos klasės realizuoja metodus skirtingai, bet naudojamos vienodai.

---

#### Inkapsuliacija

Naudojami privatūs atributai:

```python
self._base_directory
self._undo_stack
```

---

### Projektavimo šablonas

Naudojamas **Command Pattern**.

Kiekviena operacija yra atskiras objektas:

```python
operation = CreateFileOperation(manager, name)
history.execute_operation(operation)
```

Šis šablonas leidžia:

* saugoti operacijas
* įgyvendinti undo/redo
* atskirti logiką nuo vykdymo

---

### Objektų ryšiai (Kompozicija)

Klasė `OperationHistory` saugo operacijų sąrašus:

```python
self._undo_stack = []
self._redo_stack = []
```

---

### Darbas su failais

Programa dirba su failais:

```python
def write_file(self, filename, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
```

Taip pat naudojamas skaitymas:

```python
def read_file(self, filename):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
```

---

### Testavimas

Naudojami `unittest` testai.

```python
def test_write_and_read_file(self):
    self.manager.create_file("test.txt")
    self.manager.write_file("test.txt", "Hello")
    content = self.manager.read_file("test.txt")
    self.assertEqual(content, "Hello")
```

Testuojama:

* failų kūrimas
* skaitymas ir rašymas
* failų trynimas
* undo/redo

---

## Rezultatai

Sukurta programa leidžia atlikti visas numatytas failų operacijas.

Undo/redo funkcionalumas veikia teisingai ir leidžia atšaukti arba pakartoti veiksmus.

Programa veikia stabiliai ir be klaidų.

---

## Išvados

Atliekant šį darbą buvo pritaikyti visi pagrindiniai objektinio programavimo principai.

Pasiekti rezultatai:

* sukurta veikianti failų valdymo sistema
* panaudotas Command Pattern šablonas
* įgyvendintas undo/redo funkcionalumas
* sukurti vienetiniai testai
* programa turi aiškią ir modulinę struktūrą

Šis projektas parodo, kaip OOP principai gali būti pritaikyti praktikoje kuriant paprastą, bet tvarkingą programą.
