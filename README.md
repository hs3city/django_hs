# Python Hacking - Django

Projekt tworzony podczas spotkań hs3city *Python Hacking* w [Hacker:Space](http://hs3.pl/) trójmiasto.

## Przygotowanie środowiska:

### Linux / MacOS
_(ToDo: dla Windows)_

Tworzymy środowisko dla projektu:
```bash
python3 -m venv ~/projekty/venv/pythonhacking-django
```

Następnie aktywowujemy:
```bash
source ~/projekty/venv/pythonhacking-django/bin/activate
```
dla używających shell'a `fish`:
```bash
source ~/projekty/venv/pythonhacking-django/bin/activate.fish
```

## Pobranie i uruchomienie projektu

Pobranie źródeł:
```bash
cd ~/projekty/
git clone git@github.com:hs3city/pythonhacking-django.git
```

### Instalacja zależności
Pamiętaj, aby środowisko było aktywne:
```bash
cd ~/projekty/pythonhacking-django/
pip install --upgrade -r requirements.txt
```

### Przygotowanie projektu
W chwili obecnej migracje nie są przechowywane w repo.
```bash
python manage.py makemigrations
python manage.py migrate
```
Docelowo będzie można pominąć `python manage.py makemigrations`.

## Uruchomienie aplikacji

```bash
python manage.py runserver
```
