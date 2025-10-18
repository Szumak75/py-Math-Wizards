# py-Math-Wizards

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Poetry](https://img.shields.io/badge/dependency%20manager-Poetry-blue)](https://python-poetry.org/)

Console application to help children learn multiplication tables through interactive exercises.

## Description

Math Wizards is an educational console application designed to make learning multiplication tables fun and engaging. The application generates random multiplication problems (0-100), validates user answers, provides immediate feedback, and tracks performance statistics throughout the session.

### Features

- **Interactive Console Interface**: Clear terminal display with ASCII banner and encouraging messages
- **Random Problem Generation**: Multiplication problems with operands ranging from 0 to 10
- **Input Validation**: Accepts only integer answers, prompts for re-entry on invalid input
- **Instant Feedback**: Random success/failure messages to keep learning engaging
- **Session Statistics**: Real-time tracking of questions asked, correct answers, and wrong answers
- **Graceful Exit**: Ctrl+D handling with final performance report (percentage of correct answers)
- **Data Security**: Messages encrypted using ROT13 algorithm

## Requirements

- Python 3.10+
- Poetry (for dependency management)
- jsktoolbox (>=1.2.1, <2.0.0)

## Installation

### Using Poetry (Recommended)

1. Clone the repository:

```bash
git clone <repository-url>
cd py-Math-Wizards
```

2. Install dependencies:

```bash
poetry install
```

3. Run the application:

```bash
poetry run math-wizards
```

### Using the Startup Script

The project includes a bash script that automatically manages the virtual environment:

```bash
./bin/math-wizards.sh
```

The script will:

- Detect the project directory (works from any location)
- Check for existing `.venv` directory
- Create virtual environment from `requirements.txt` if needed
- Activate environment and launch the application

### Manual Installation

1. Create virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python3 -m py_math_wizards.main
```

## Usage

After starting the application:

1. The terminal will clear and display the Math Wizards banner
2. You'll see a random greeting message encouraging you to practice
3. Answer each multiplication problem (format: `2 * 8 = _`)
4. Enter only integer numbers (validation enforced)
5. Receive immediate feedback on your answer
6. Continue solving problems - statistics are tracked automatically
7. Press Ctrl+D at any time to see your final performance report

### Example Session

```
╔═══════════════════════════════════╗
║       MATH WIZARDS v0.1.0         ║
║   Multiplication Table Practice   ║
╚═══════════════════════════════════╝

Let's practice multiplication! You've got this!

Question 1:
3 * 7 = 21
✓ Excellent work! That's correct!

Question 2:
5 * 9 = 40
✗ Not quite. The correct answer is 45. Keep trying!

^C
Session Summary:
Questions asked: 2
Correct answers: 1
Wrong answers: 1
Success rate: 50.00%
```

## Project Structure

```
py-Math-Wizards/
├── bin/
│   └── math-wizards.sh        # Startup script
├── py_math_wizards/
│   ├── __init__.py
│   ├── banner.py              # ASCII banner generation
│   ├── greetings.py           # Welcome messages
│   ├── main.py                # Main application logic
│   ├── messages.py            # Success/failure messages (ROT13)
│   ├── question_generator.py  # Problem generation
│   └── statistics.py          # Performance tracking
├── tests/
│   └── test_*.py              # Unit tests
├── .gitignore
├── AGENTS.md                  # AI configuration
├── LICENSE
├── poetry.lock
├── pyproject.toml             # Project configuration
├── README.md
└── requirements.txt
```

## Development

### Setup Development Environment

```bash
poetry install
```

### Code Quality Tools

The project uses the following tools (configured in `pyproject.toml`):

- **black**: Code formatting

  ```bash
  poetry run black .
  ```

- **isort**: Import sorting

  ```bash
  poetry run isort .
  ```

- **pycodestyle**: PEP 8 compliance

  ```bash
  poetry run pycodestyle .
  ```

- **flake8**: Linting

  ```bash
  poetry run flake8 .
  ```

- **mypy**: Type checking
  ```bash
  poetry run mypy .
  ```

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage report
poetry run pytest --cov=py_math_wizards

# Run specific test file
poetry run pytest tests/test_main.py
```

### Code Style

The project follows:

- PEP 8 style guide
- Google-style docstrings
- Type hints (PEP 484)
- Black formatting (88 character line length)
- Single quotes for strings (unless double quotes required)
- Object-oriented architecture
  - Each class inherits from `jsktoolbox.attribtool.NoNewAttributes`
  - Class variables through `jsktoolbox.basetool.BData`
  - Exception handling via `jsktoolbox.raisetool.Raise.error()`

## Architecture

The application follows object-oriented design principles:

- **MathWizards** (`main.py`): Main application controller, manages session lifecycle and signal handling
- **QuestionGenerator** (`question_generator.py`): Generates random multiplication problems
- **Statistics** (`statistics.py`): Tracks and reports performance metrics
- **Banner** (`banner.py`): Generates ASCII art banner
- **Greetings** (`greetings.py`): Provides randomized greeting messages
- **Messages** (`messages.py`): Manages success/failure feedback (ROT13 encrypted)

Each class is in a separate module and uses lazy imports for better performance.

## Contributing

1. Follow the code style guidelines in `AGENTS.md`
2. Write tests for new functionality (target: >80% coverage)
3. Run linters and formatters before committing
4. Use conventional commit messages: `type(scope): subject`
5. Ensure all tests pass

## Version History

- **0.1.0** (2025-10-18): Initial release
  - Core multiplication practice functionality
  - Interactive console interface
  - Statistics tracking
  - Signal handling (Ctrl+D)
  - Unit tests (26 tests, 100% pass)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Jacek 'Szumak' Kotlarski  
Email: szumak@virthost.pl  
GitHub: [@Szumak75](https://github.com/Szumak75)

## Acknowledgments

- Built with [jsktoolbox](https://github.com/Szumak75/jsktoolbox) - A collection of utilities for Python projects
- Developed with Python 3.10+ and Poetry
