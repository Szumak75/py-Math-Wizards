# py-Math-Wizard projekt

- język projektu: angielski
- język programowania: python3 >=3.10, <4
- moduł podstawowy w zależnościach: jsktoolbox
- menadżer projektu: poetry
- testy jednostkowe: pytest
- repozytorium: git
- foldery projektu: bin, tests, py_math_wizard
- foldery wykluczone z repozytorium: tmp

# Zadanie pierwsze

- Na podstawie szablonu ./AGENTS-TEMPLATE.md wygeneruj konfogurację projektową AGENTS.md i wykonaj do niej link symboliczny GEMINI.md
- Dodaj do pyproject.toml wszystkie niezbędne zależności projektowe z kategorii dev i przeprowadź aktualizację środowiska wirtualnego.
- Przy każdej zmianie dbaj o aktualizację AGENTS.md
- Wygeneruj .gitignore stosownie do założeń projektowych

# Zadanie drugie

Celem projektu jest stworzenie aplikacji konsolowej, która będzie pomagała dzieciom w nauce tabliczki mnożenia w zakresie od 0 do 100 na liczbach całkowitych.

## Założenia interfejsu użytkownika:

- start aplikacji w terminalu znakowym czyści terminal, wyświetla na nim baner startowy aplikacji (ASCII), poniżej wita użytkownika jednozdaniową zachętą do wykonywania ćwiczenia (najlepiej by była losowana z dużej tablicy uprzednio przygotowanych zwrotów) następnie przechodzi do części zadaniowej, na przykład przed promptem podając zadanie: 2 * 8 = _ - w miejscu '_' użytkownik wpisuje swoją odpowiedź i naciska [enter]. Program sprawdza poprawność i informuje użytkownika o sukcesie lub porażce w sposób opisany w punkcie kolejnym. Rzeczą oczywistą jest, że program oczekuje w odpowiedzi liczb, jeżeli otrzyma odpowiedź z poza zakresu liczbowego, informuje użytkownika, że oczekuje odpowiedzi w postaci liczby całkowitej (w tym przypadku) i ponawia to samo pytanie nie traktują odpowiedzi jako błędną ani dobrą.
- w katalogu py_math_wizards/data znajdują się dwa pliki: ok.txt oraz bad.txt zawierające listę proponowanych odpowiedzi potwierdzających sukces jak i porażkę użytkownika podczas rozwiązywania zadania, powinny być losowo wyświetlane w zależności od tego czy odpowiedź była poprawna czy błędna.
- program zlicza ilość wygenerowanych zadań, ilość odpowiedzi poprawnych oraz ilość odpowiedzi błędnych.
- jeżeli użytkownik naciśnie [ctrl]-[c] program przechwytuje to żądanie i przechodzi w tryb kończenia swojej pracy. Przed wyjściem na konsoli wyświetla raport statystyczny sesji: ilość zadań oraz procent odpowiedzi poprawnych.

## Założenia implementacyjne:

- całość programu napisana w architekturze obiektowej, każda klasa w osobnym module. Klasa główna w module 'py_match_wizard.main' lub 'py_math_wizard' przy użyciu leniwych importów.
- każda klasa ma być dziedziczona z jsktoolbox.attribtool.NoNewAttributes, w przypadku potrzeby korzystania ze zmiennych klasowych należy dziedziczyć z klasy kontenerowej jsktoolbox.basetool.BData i używać jej mechanizmów tworzenia zmiennych w słownikach.
- wszystko co się da powinno być pokryte testami jednostkowymi
- testy jednostkowe napisane w architekturze obiektowej, klasy dziedziczone z unittest.TestCase i podobnych zależnie od potrzeby.
- zawartość plików ok.txt oraz bad.txt ma się znaleźć na zmiennej List wewnątrz klasy obsługujących te komentarze. Każdy z rekordów ma być szyfrowany metodą rot13 by w pliku źródłowym nie był łatwo rozpoznawalny. Jeżeli zostanie podjęta decyzja o umieszczeniu na kolejnych listach innych wariantów odpowiedzi należy przyjąć taką samą metodologię. Program nie powinien otwierać zewnętrznych plików do odczytu bądź zapisu w trakcie swojego działania (poza stdin i stdout).
- ewentualne wyjątki mają być rzucane po uprzednim przeformatowaniu przy pomocy jsktoolbox.raisetool.Raise.error().
- należy wygenerować plik 'requirements.txt' w głównym katalogu projektu.
- w katalogu ./bin ma zostać wygenerowany skrypt startowy. Jego zadania:

    - niezależnie skąd zostanie uruchomiony: folder 'bin' w katalogu projektu, czy symlink gdziekolwiek w systemie, ma sprawdzić czy w katalogu projektu istnieje wirtualne środowisko '.venv'
    - jeżeli brak '.venv' skrypt generuje go na podstawie 'requirements.txt' 
    - jeżeli '.venv' już istnieje, aktywowane jest środowisko wirtualne i w nim uruchamiana jest aplikacja.
