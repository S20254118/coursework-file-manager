# Failų valdymo sistema (OOP kursinis darbas)

## Įvadas

Šio kursinio darbo tikslas – sukurti paprastą failų valdymo sistemą, naudojant Python programavimo kalbą ir objektinio programavimo (OOP) principus.

Programa leidžia atlikti pagrindines failų operacijas (kurti, skaityti, rašyti, pervadinti, trinti) bei turi undo/redo funkcionalumą, kuris leidžia atšaukti arba pakartoti veiksmus.

---

## Programos struktūra

Projektas susideda iš kelių pagrindinių dalių:

* `main.py` – pagrindinė programa su vartotojo sąsaja
* `file_manager.py` – atsakingas už darbą su failais
* `operations.py` – failų operacijų klasės
* `history.py` – operacijų istorijos valdymas (undo/redo)
* `tests/` – vienetiniai testai

---

## OOP principų taikymas

### Abstrakcija

Naudojama abstrakti klasė `FileOperation`, kuri apibrėžia bendrą visų operacijų struktūrą.

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

### Paveldėjimas

Konkrečios operacijos paveldi bazinę klasę.

```python
class CreateFileOperation(FileOperation):
    def __init__(self, file_manager, filename):
        super().__init__(file_manager)
        self._filename = filename

    def execute(self):
        self._file_manager.create_file(self._filename)
```

---

### Polimorfizmas

Visos operacijos vykdomos naudojant tuos pačius metodus `execute()` ir `undo()`.

```python
history.execute_operation(operation)
history.undo()
```

Skirtingos operacijos realizuoja šiuos metodus skirtingai, bet naudojamos vienodai.

---

### Inkapsuliacija

Naudojami privatūs atributai, kurie saugo vidinę objekto būseną.

```python
self._base_directory = Path(base_directory)
self._undo_stack = []
self._redo_stack = []
```

---

## Projektavimo šablonas

Šiame projekte naudojamas **Command Pattern**.

Kiekviena operacija yra atskiras objektas:

```python
operation = CreateFileOperation(manager, name)
history.execute_operation(operation)
```

Šis šablonas leidžia:

* saugoti operacijų istoriją
* įgyvendinti undo/redo funkcionalumą
* atskirti operacijų logiką nuo jų vykdymo

---

## Objektų ryšiai (Kompozicija)

Klasė `OperationHistory` saugo operacijų sąrašus:

```python
class OperationHistory:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []
```

Tai yra kompozicijos pavyzdys, kai vienas objektas valdo kitus objektus.

---

## Darbas su failais (I/O)

Programa dirba su failais naudojant Python funkcijas.

```python
def write_file(self, filename, content):
    path = self._get_path(filename)
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

## Testavimas

Projektui sukurti vienetiniai testai naudojant `unittest`.

Pavyzdys:

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

---

## Rezultatai

Programa veikia stabiliai ir leidžia atlikti visas numatytas funkcijas.

Undo/redo funkcionalumas veikia teisingai ir leidžia atšaukti paskutinius veiksmus.

---

## Išvados

Atliekant šį darbą buvo pritaikyti pagrindiniai objektinio programavimo principai.

Pasiekti rezultatai:

* sukurta veikianti failų valdymo sistema
* panaudotas projektavimo šablonas
* įgyvendintas undo/redo mechanizmas
* programa yra aiškios struktūros ir lengvai plečiama

Šis projektas parodo, kaip OOP principai gali būti naudojami praktikoje kuriant realias sistemas.
