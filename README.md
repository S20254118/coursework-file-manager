
# Failų valdymo sistema (OOP kursinis darbas)

Šis projektas buvo sukurtas kaip kursinis darbas, siekiant pritaikyti objektinio programavimo principus praktikoje.

Sistema leidžia vartotojui atlikti pagrindines failų operacijas ir turi undo/redo funkcionalumą, kuris leidžia atšaukti ir pakartoti veiksmus.

---

## Funkcionalumas

- Sukurti failą
- Rašyti į failą
- Skaityti failą
- Pervadinti failą
- Ištrinti failą
- Peržiūrėti failų sąrašą
- Undo / Redo operacijos
- Klaidų apdorojimas

---

## Kaip paleisti

### Paleisti programą

```bash
python main.py
````

### Paleisti testus

```bash
python -m unittest discover -s tests
```

---

## OOP principai

### Abstrakcija

Naudojama abstrakti klasė, kuri apibrėžia bendrą operacijų struktūrą.

```python
class FileOperation(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass
```

### Paveldėjimas

Konkrečios operacijos paveldi bazinę klasę.

```python
class CreateFileOperation(FileOperation):
    def execute(self):
        self._file_manager.create_file(self._filename)
```

### Polimorfizmas

Visos operacijos vykdomos per tą pačią sąsają.

```python
operation.execute()
operation.undo()
```

### Inkapsuliacija

Naudojami privatūs atributai.

```python
self._base_directory
self._undo_stack
```

---

## Projektavimo šablonas

### Command Pattern

Naudojamas Command šablonas, kuris leidžia pateikti operacijas kaip objektus.

Tai leidžia:

* saugoti operacijas istorijoje
* įgyvendinti undo/redo
* atskirti logiką nuo vykdymo

```python
history.execute_operation(operation)
history.undo()
```

---

## Objektų ryšiai

Sistema naudoja kompoziciją. Klasė `OperationHistory` saugo operacijų istoriją.

```python
self._undo_stack = []
self._redo_stack = []
```

---

## Darbas su failais

Programa dirba su failais naudojant Python.

```python
with open(path, "w", encoding="utf-8") as file:
    file.write(content)
```

Galimos operacijos:

* skaitymas
* rašymas
* trynimas
* pervadinimas

---

## Testavimas

Naudojami `unittest` testai.

Testuojama:

* failų kūrimas
* skaitymas ir rašymas
* failų trynimas
* undo/redo funkcionalumas

---

## Projekto struktūra

```text
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

## Išvados

Projektas parodo, kaip OOP principai gali būti pritaikyti praktikoje.

Pasiekimai:

* aiški struktūra
* panaudotas projektavimo šablonas
* modulinė architektūra
* stabilus darbas su failais
* įgyvendintas undo/redo mechanizmas

# Failų valdymo sistema (OOP kursinis darbas)

## Įvadas

Šio kursinio darbo tikslas – sukurti paprastą failų valdymo sistemą, naudojant Python programavimo kalbą ir objektinio programavimo (OOP) principus.

Programa leidžia atlikti pagrindines failų operacijas: kurti, skaityti, rašyti, pervadinti ir trinti failus. Taip pat programa turi undo/redo funkcionalumą, kuris leidžia atšaukti arba pakartoti veiksmus.

---

## Programos struktūra

Projektas susideda iš kelių pagrindinių dalių:

* `main.py` – pagrindinė programa su vartotojo sąsaja.
* `file_manager.py` – klasė, atsakinga už darbą su failais.
* `operations.py` – failų operacijų klasės.
* `history.py` – operacijų istorijos valdymas.
* `tests/` – vienetiniai testai.

---

## OOP principų taikymas

### Abstrakcija

Abstrakcija naudojama klasėje `FileOperation`. Ji apibrėžia bendrą visų operacijų struktūrą.

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

Ši klasė nurodo, kad kiekviena operacija privalo turėti `execute()` ir `undo()` metodus.

---

### Paveldėjimas

Konkrečios operacijos paveldi bazinę klasę `FileOperation`.

```python
class CreateFileOperation(FileOperation):
    def __init__(self, file_manager, filename):
        super().__init__(file_manager)
        self._filename = filename

    def execute(self):
        self._file_manager.create_file(self._filename)
```

Tai leidžia kiekvienai operacijai turėti bendrą struktūrą, bet skirtingą veikimo logiką.

---

### Polimorfizmas

Polimorfizmas pasireiškia tuo, kad skirtingos operacijos turi tuos pačius metodus `execute()` ir `undo()`, tačiau jų veikimas skiriasi.

```python
history.execute_operation(operation)
history.undo()
```

Programa gali naudoti skirtingas operacijas vienodu būdu, nes visos jos turi tą pačią sąsają.

---

### Inkapsuliacija

Inkapsuliacija naudojama saugant vidinius klasės duomenis. Pavyzdžiui, naudojami atributai su pabraukimu:

```python
self._base_directory = Path(base_directory)
self._undo_stack = []
self._redo_stack = []
```

Tokie atributai nėra skirti tiesiogiai keisti iš išorės. Su jais dirbama per klasės metodus.

---

## Projektavimo šablonas

Šiame projekte naudojamas **Command Pattern**.

Kiekviena failo operacija yra atskiras objektas:

```python
operation = CreateFileOperation(manager, name)
history.execute_operation(operation)
```

Command Pattern pasirinktas todėl, kad jis labai tinka undo/redo funkcionalumui. Kiekviena operacija žino, kaip atlikti veiksmą ir kaip jį atšaukti.

---

## Objektų ryšiai

Klasė `OperationHistory` saugo operacijų sąrašus:

```python
class OperationHistory:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []
```

Tai yra kompozicijos pavyzdys, nes vienas objektas saugo ir valdo kitus objektus.

---

## Darbas su failais

Programa dirba su realiais failais. Pavyzdžiui, failo rašymas atliekamas taip:

```python
def write_file(self, filename, content):
    path = self._get_path(filename)
    if not path.exists():
        raise FileNotFoundError(f"File '{filename}' not found.")
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
```

Failo skaitymas:

```python
def read_file(self, filename):
    path = self._get_path(filename)
    if not path.exists():
        raise FileNotFoundError(f"File '{filename}' not found.")
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
```

Programa palaiko failų kūrimą, skaitymą, rašymą, pervadinimą ir trynimą.

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
* pervadinimas
* undo/redo funkcionalumas

---

## Rezultatai

Programa veikia stabiliai ir leidžia atlikti visas numatytas failų operacijas.

Undo/redo funkcionalumas leidžia atšaukti paskutinį veiksmą arba pakartoti atšauktą veiksmą.

Naudojant Command Pattern, programos struktūra tapo aiškesnė ir lengviau plečiama.

---

## Išvados

Atliekant šį darbą buvo pritaikyti pagrindiniai objektinio programavimo principai.

Pasiekti rezultatai:

* sukurta veikianti failų valdymo sistema
* panaudoti visi keturi OOP principai
* panaudotas Command Pattern projektavimo šablonas
* įgyvendintas undo/redo mechanizmas
* sukurti vienetiniai testai
