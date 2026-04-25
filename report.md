# Failų valdymo sistema (OOP kursinis darbas)

## Įvadas

Šio kursinio darbo tikslas – sukurti paprastą failų valdymo sistemą naudojant Python programavimo kalbą ir objektinio programavimo (OOP) principus.

Programa leidžia atlikti pagrindines failų operacijas: kurti, skaityti, rašyti, pervadinti ir trinti failus. Taip pat įgyvendintas undo/redo funkcionalumas, kuris leidžia atšaukti arba pakartoti veiksmus.

Darbo metu buvo siekiama ne tik sukurti veikiančią programą, bet ir pritaikyti teorines OOP žinias praktikoje.

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

Šie principai padeda sukurti lankstesnę ir lengviau prižiūrimą programą.

---

### Projektavimo šablonas

Šiame projekte naudojamas **Command Pattern**.

Kiekviena operacija yra atskiras objektas:

```python
operation = CreateFileOperation(manager, name)
history.execute_operation(operation)
```

Šis šablonas leidžia:

* saugoti operacijas
* įgyvendinti undo/redo
* atskirti logiką nuo vykdymo

#### Sustiprinta analizė

Command Pattern pasirinktas todėl, kad jis leidžia kiekvieną veiksmą modeliuoti kaip atskirą objektą su metodais `execute()` ir `undo()`.

Toks sprendimas leidžia išvengti sudėtingos logikos, kuri atsirastų naudojant paprastą procedūrinį metodą. Kiekviena operacija pati „žino“, kaip ją atlikti ir kaip ją atšaukti.

Tai leidžia:

* lengvai įgyvendinti undo/redo be sudėtingų sąlygų
* išplėsti sistemą pridedant naujas operacijas nekeičiat esamos logikos
* sumažinti komponentų priklausomybę

---

### Objektų ryšiai (Kompozicija)

Klasė `OperationHistory` saugo operacijų sąrašus:

```python
self._undo_stack = []
self._redo_stack = []
```

Tai yra kompozicijos pavyzdys, kai vienas objektas valdo kitus objektus.

---

### Architektūriniai sprendimai

Projektas padalintas į atskirus modulius:

* `file_manager.py` – darbas su failais
* `operations.py` – operacijos
* `history.py` – istorija

Tai atitinka **Single Responsibility Principle**, nes kiekvienas modulis turi vieną atsakomybę.

Tokiu būdu:

* lengviau testuoti sistemą
* paprasčiau keisti kodą
* aiškesnė programos struktūra

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

Sukurta sistema leidžia atlikti visas numatytas funkcijas.

Undo/redo mechanizmas veikia stabiliai net atliekant kelias operacijas iš eilės.

Programa buvo ištestuota naudojant skirtingus scenarijus, ir visos funkcijos veikė teisingai.

---

## Išvados

Atliekant šį darbą buvo pritaikyti pagrindiniai objektinio programavimo principai.

Darbo metu buvo įgyta praktinė patirtis taikant OOP principus realiame projekte.

Pagrindinė išvada – teisingai parinkta architektūra (OOP + Command Pattern) leidžia:

* supaprastinti sudėtingą funkcionalumą (undo/redo)
* padidinti programos lankstumą
* sumažinti klaidų tikimybę

Pasiekti rezultatai:

* sukurta veikianti failų valdymo sistema
* panaudotas Command Pattern šablonas
* įgyvendintas undo/redo funkcionalumas
* sukurti vienetiniai testai
* programa turi aiškią ir modulinę struktūrą

Šis projektas parodo, kaip OOP principai gali būti pritaikyti praktikoje kuriant paprastą, bet tvarkingą programą.
