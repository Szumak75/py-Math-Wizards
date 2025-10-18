# Konfiguracja AI Agents - py-Math-Wizards

## Informacje o projekcie

- **Nazwa projektu**: `py-Math-Wizards`
- **Główny język**: `Python`
- **Wersja języka**: `3.10+`
- **System zarządzania**: `Poetry`
- **Repozytorium**: `git`

---

## Konfiguracja plików

### Automatyczna detekcja typu projektu

**files.include** - Pliki źródłowe i testy:

- `**/*.py`
- `tests/**/*.py`
- `test_*.py`
- `README.md`
- `docs/**/*.md`
- `*.md`
- `pyproject.toml`

**files.exclude** - Wykluczenia:

- `.venv/**`
- `venv/**`
- `env/**`
- `.pytest_cache/**`
- `__pycache__/**`
- `*.pyc`
- `*.pyo`
- `dist/**`
- `build/**`
- `*.egg-info/**`
- `.git/**`
- `.gitignore`
- `.vscode/**`
- `.idea/**`
- `*.swp`
- `*~`
- `*.log`
- `*.tmp`
- `tmp/**`
- `temp/**`
- `node_modules/**`
- `package-lock.json`

---

## Instrukcje dotyczące zachowania

### Język i zarządzanie projektem

**Dla projektów Python z Poetry:**

- **Język**: Python 3.10+
- **Zarządzanie projektem**: Projekt używa Poetry
- **Uruchamianie narzędzi**: `poetry run <polecenie>` (np. `poetry run pytest`)
- **Instalacja zależności**: `poetry install`
- **Aktualizacja**: `poetry update`
- **Moduł podstawowy**: jsktoolbox@^1.2.1

### Styl kodowania

#### Python

**Formatowanie i walidacja:**

- **Formatter**: `black` - automatyczne formatowanie kodu
  - Uruchamianie: `poetry run black .`
  - Konfiguracja: Sprawdź `[tool.black]` w `pyproject.toml`
- **Linter**: `pycodestyle` lub `flake8` - zgodność z PEP 8
  - Uruchamianie: `poetry run pycodestyle .` lub `poetry run flake8 .`
- **Type checking**: `mypy` - sprawdzanie typów
  - Uruchamianie: `poetry run mypy .`
- **Import sorting**: `isort` - sortowanie importów
  - Uruchamianie: `poetry run isort .`

**Konwencje kodowania:**

- Przestrzegaj PEP 8 (Style Guide for Python Code)
- Dodawaj adnotacje typów do nowych funkcji i metod
- Używaj type hints zgodnie z PEP 484
- Preferuj pojedyncze cudzysłowy `'string'`, chyba że podwójne są wymagane
- Maksymalna długość linii: 88 znaków (black default)
- Używaj f-strings do formatowania stringów (Python 3.6+)
- Każda klasa dziedziczy z jsktoolbox.attribtool.NoNewAttributes
- Dla zmiennych klasowych dziedziczyć z jsktoolbox.basetool.BData
- Używaj leniwych importów dla klas z py_math_wizards

**Docstringi:**

- Format: Google style
- Struktura: Krótka linia streszczenia, następnie sekcje
- Sekcje: `### Arguments`, `### Returns`, `### Raises`, `### Examples`
- Język: Angielski (kod i dokumentacja techniczna)

**Architektura:**

- Całość programu napisana w architekturze obiektowej
- Każda klasa w osobnym module
- Klasa główna w module 'py_math_wizards.main'
- Import klas z 'py_math_wizards' przy użyciu leniwych importów
- Każda klasa dziedziczy z jsktoolbox.attribtool.NoNewAttributes
- Zmienne klasowe przez jsktoolbox.basetool.BData
- Wyjątki przez jsktoolbox.raisetool.Raise.error()

### Testowanie

#### Python

**Framework i organizacja:**

- **Framework**: `pytest` i `unittest`
- **Lokalizacja testów**: `tests/` w głównym katalogu
- **Nazewnictwo**: `test_*.py`
- **Uruchamianie**: `poetry run pytest`
- **Pokrycie kodu**: `poetry run pytest --cov=py_math_wizards`

**Konwencje testowe:**

- Klasy testowe dziedziczą po `unittest.TestCase`
- Architektura obiektowa dla testów
- Jeden test = jedna funkcjonalność
- Używaj fixtures dla konfiguracji testowej
- Zapewnij pokrycie testami każdej nowej funkcjonalności (cel: >80%)

### Obsługa błędów

#### Python

**Strategia obsługi błędów:**

- Używaj specyficznych wyjątków zamiast ogólnego `Exception`
- Twórz własne klasy wyjątków gdy potrzebne
- Dokumentuj wyjątki w docstringach (sekcja `### Raises`)
- Używaj `try-except-finally` odpowiednio
- Unikaj "gołych" `except:` - zawsze określ typ wyjątku
- Loguj błędy przed re-raise lub obsługą

**Mechanizm projektu:**

```python
from jsktoolbox.raisetool import Raise
raise Raise.error(message, exception_type, class_name, frame)
```

### Kontrola wersji (Git)

**Konwencje commitów:**

- Format: `type(scope): subject` (Conventional Commits)
- Typy: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Przykład: `feat(parser): add support for JSON input`
- Długość subject: max 50 znaków
- Body (opcjonalnie): szczegółowy opis po pustej linii

### Dokumentacja

**Struktura dokumentacji:**

- `README.md` - główny plik projektu (co, dlaczego, jak używać)
- `CHANGELOG.md` - historia zmian (Keep a Changelog format)
- `AGENTS.md` - konfiguracja AI

**Formatowanie dokumentacji Markdown:**

- **Tool**: `prettier` - formatowanie plików Markdown
  - Uruchamianie: `npm run format:md`
  - Sprawdzanie: `npm run format:check`
  - Konfiguracja: `.prettierrc.json`
  - Instalacja: `npm install` (prettier zainstalowany w `~/.local/node_modules/`)
- Zachowaj czytelność i spójność formatowania
- Używaj 88 znaków szerokości linii (zgodnie z black)
- Preserve prose wrapping dla plików `.md`

### Ogólne zalecenia

**Komunikacja z AI Assistant:**

- **Język odpowiedzi**: Polski
- **Język kodu**: Angielski (komentarze, nazwy zmiennych, dokumentacja)
- **Język dokumentacji projektu**: Angielski (README, docs)
- **Język konfiguracji**: Polski (AGENTS.md)

**Podejście do zmian:**

- Zachowuj zwięzłą, techniczną formę odpowiedzi
- Przy zmianach obejmujących wiele plików przedstaw plan i poproś o akceptację
- Testuj zmiany przed commitem
- Dokumentuj nieoczywiste decyzje projektowe
- Refaktoryzuj kod zgodnie z DRY (Don't Repeat Yourself)
- Preferuj czytelność nad "sprytne" rozwiązania

**Code Review Checklist:**

- [ ] Kod jest zgodny z konwencjami projektu
- [ ] Testy zostały dodane/zaktualizowane
- [ ] Dokumentacja jest aktualna
- [ ] Brak ostrzeżeń z linterów
- [ ] Zmiany nie psują istniejącej funkcjonalności
- [ ] Obsługa błędów jest poprawna
- [ ] Kod jest czytelny i zrozumiały

---

## Szablony dokumentacji

### Python Docstring Template

#### Module-level Docstring

```python
"""
Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
Created: YYYY-MM-DD

Purpose: Short, one-line summary of the module's purpose.

[Optional: More detailed description of the module's functionality,
its components, and how they fit into the larger project.]
"""
```

#### Class-level Docstring

```python
"""Short, one-line summary of the class's purpose.

[Optional: More detailed description of the class's responsibilities,
design choices, and its role (e.g., utility, data structure).]
"""
```

#### Function/Method-level Docstring

````python
"""Short, one-line summary of what the function does.

[Optional: More detailed explanation of the function's logic,
its use cases, or any important algorithms used.]

### Arguments:
* arg1: [type] - Description of the first argument.
* arg2: Optional[[type]] - Description of the second, optional argument. Defaults to [DefaultValue].

### Returns:
[type] - Description of the returned value.

### Raises:
* [ExceptionType]: Description of the condition that causes this exception to be raised.

### Examples:
```python
>>> function_name(arg1, arg2)
expected_result
````

"""

````

---

## Narzędzia deweloperskie

### Python Tools

**Podstawowe:**

- `black` - code formatter
- `pytest` - testing framework
- `pycodestyle` - linting
- `flake8` - linting
- `mypy` - type checking
- `isort` - import sorting
- `pytest-cov` - code coverage

**Poetry dependencies:**

```toml
[tool.poetry.group.dev.dependencies]
black = "^24.0.0"
pytest = "^8.0.0"
pycodestyle = "^2.12.0"
flake8 = "^7.0.0"
mypy = "^1.11.0"
isort = "^5.13.0"
pytest-cov = "^5.0.0"
````

---

## Specyfika projektu

### Struktura katalogów

- `bin/` - skrypty startowe
- `tests/` - testy jednostkowe
- `py_math_wizards/` - kod źródłowy aplikacji
- `py_math_wizards/data/` - dane (ok.txt, bad.txt)
- `tmp/` - folder wykluczony z repozytorium

### Wymagania implementacyjne

- Całość w architekturze obiektowej
- Każda klasa w osobnym module
- Klasa główna: `py_math_wizards.main`
- Leniwne importy z `py_math_wizards`
- Dziedziczenie z `jsktoolbox.attribtool.NoNewAttributes`
- Zmienne klasowe przez `jsktoolbox.basetool.BData`
- Szyfrowanie danych metodą rot13
- Wyjątki przez `jsktoolbox.raisetool.Raise.error()`
- Brak odczytu/zapisu zewnętrznych plików (poza stdin/stdout)

### Funkcjonalność aplikacji

**Cel**: Aplikacja konsolowa do nauki tabliczki mnożenia (0-100, liczby całkowite)

**Interfejs użytkownika:**

- Czyszczenie terminala przy starcie
- Banner ASCII
- Losowane zachęty do ćwiczeń
- Format zadania: `2 * 8 = _`
- Walidacja odpowiedzi (tylko liczby całkowite)
- Losowe komunikaty sukcesu/porażki z plików ok.txt/bad.txt
- Statystyki: liczba zadań, odpowiedzi poprawnych/błędnych
- Obsługa Ctrl+C: raport końcowy z procentem poprawnych odpowiedzi

**Dane:**

- Komunikaty sukcesu/porażki zaszyfrowane rot13 w kodzie
- Źródło: pliki `py_math_wizards/data/ok.txt` i `py_math_wizards/data/bad.txt`

### Skrypt startowy (bin/)

**Wymagania:**

- Detekcja katalogu projektu (niezależnie od miejsca uruchomienia)
- Sprawdzenie istnienia `.venv`
- Utworzenie `.venv` z `requirements.txt` jeśli brak
- Aktywacja środowiska i uruchomienie aplikacji

---

## Wersjonowanie

- **Wersja**: 1.1.0
- **Data utworzenia**: 2025-10-18
- **Autor**: Jacek 'Szumak' Kotlarski
- **Ostatnia aktualizacja**: 2025-10-18

### Historia zmian

- `1.1.0` (2025-10-18): Dodano formatowanie dokumentów Markdown
  - Dodano prettier jako narzędzie do formatowania plików Markdown
  - Utworzono package.json z skryptami npm
  - Utworzono konfigurację .prettierrc.json
  - Utworzono .prettierignore
  - Zaktualizowano .gitignore (node_modules, package-lock.json)
  - Zaktualizowano AGENTS.md (sekcja formatowania dokumentacji)
  - Sformatowano README.md i AGENTS.md przez prettier
- `1.0.0` (2025-10-18): Utworzenie konfiguracji projektu py-Math-Wizards
  - Utworzono AGENTS.md i link symboliczny GEMINI.md
  - Dodano zależności dev do pyproject.toml
  - Wygenerowano .gitignore
  - Wygenerowano requirements.txt
  - Zaimplementowano aplikację Math Wizards:
    - Moduł banner.py - banner ASCII
    - Moduł greetings.py - powitania
    - Moduł messages.py - komunikaty sukcesu/porażki (ROT13)
    - Moduł statistics.py - statystyki sesji
    - Moduł question_generator.py - generator pytań
    - Moduł main.py - główna aplikacja
  - Utworzono testy jednostkowe (26 testów, 100% pass, coverage 55%)
  - Utworzono skrypt startowy bin/math-wizards.sh
  - Kod sformatowany przez black i isort
