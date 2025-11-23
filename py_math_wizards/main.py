"""
Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
Created: 2025-10-18

Purpose: Main application module for Math Wizards.
"""

from inspect import currentframe
import os
from re import S
import signal
import sys
from typing import TYPE_CHECKING, List, Optional

from jsktoolbox.basetool import BData
from jsktoolbox.raisetool import Raise
from jsktoolbox.attribtool import ReadOnlyClass

if TYPE_CHECKING:
    from py_math_wizards.question_generator import QuestionGenerator
    from py_math_wizards.statistics import Statistics


class _Keys(object, metaclass=ReadOnlyClass):
    """Keys class for internal purpose only."""

    STATISTICS = "statistics"
    GENERATOR = "generator"
    RUNNING = "running"
    ARC_A = "arc_a"
    ARC_B = "arc_b"


class MathWizards(BData):
    """Main application class for Math Wizards."""

    def __init__(self) -> None:
        """Initialize MathWizards application."""
        from py_math_wizards.question_generator import QuestionGenerator
        from py_math_wizards.statistics import Statistics

        self._set_data(
            key=_Keys.STATISTICS, value=Statistics(), set_default_type=Statistics
        )
        self._set_data(
            key=_Keys.GENERATOR,
            value=QuestionGenerator(0, 10),
            set_default_type=QuestionGenerator,
        )
        self._set_data(key=_Keys.RUNNING, value=True, set_default_type=bool)

        # Setup signal handler for Ctrl+C
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

    @property
    def archive_a(self) -> List[int]:
        """Get the archive A value.

        ### Returns:
        List[int] - The archive A value.
        """
        arc_a: Optional[List[int]] = self._get_data(key=_Keys.ARC_A, default_value=[])
        if arc_a is None:
            raise Raise.error(
                "Archive A is not initialized",
                RuntimeError,
                self._c_name,
                currentframe(),
            )
        return arc_a

    @archive_a.setter
    def archive_a(self, value: int) -> None:
        """Set the archive A value.

        ### Arguments:
        * value: int - The new archive A value.
        """
        if not isinstance(value, int):
            raise Raise.error(
                "Archive A must be an integer",
                TypeError,
                self._c_name,
                currentframe(),
            )
        arch_a = self._get_data(key=_Keys.ARC_A)
        if arch_a is None:
            arch_a = []
            arch_a.append(value)
            self._set_data(key=_Keys.ARC_A, value=arch_a)
        else:
            arch_a.append(value)
            if len(arch_a) > 5:
                arch_a.pop(0)

    @property
    def archive_b(self) -> List[int]:
        """Get the archive A value.

        ### Returns:
        List[int] - The archive B value.
        """
        arc_b: Optional[List[int]] = self._get_data(key=_Keys.ARC_B, default_value=[])
        if arc_b is None:
            raise Raise.error(
                "Archive B is not initialized",
                RuntimeError,
                self._c_name,
                currentframe(),
            )
        return arc_b

    @archive_b.setter
    def archive_b(self, value: int) -> None:
        """Set the archive B value.
        ### Arguments:
        * value: int - The new archive B value.
        """
        if not isinstance(value, int):
            raise Raise.error(
                "Archive B must be an integer",
                TypeError,
                self._c_name,
                currentframe(),
            )
        arch_b = self._get_data(key=_Keys.ARC_B)
        if arch_b is None:
            arch_b = []
            arch_b.append(value)
            self._set_data(key=_Keys.ARC_B, value=arch_b)
        else:
            arch_b.append(value)
            if len(arch_b) > 5:
                arch_b.pop(0)

    @property
    def statistics(self) -> "Statistics":
        """Get the statistics object.

        ### Returns:
        Statistics - The statistics object.
        """
        statistics: Optional[Statistics] = self._get_data(
            key=_Keys.STATISTICS, default_value=None
        )
        if statistics is None:
            raise Raise.error(
                "Statistics object is not initialized",
                RuntimeError,
                self._c_name,
                currentframe(),
            )
        return statistics

    @property
    def generator(self) -> "QuestionGenerator":
        """Get the question generator object.

        ### Returns:
        QuestionGenerator - The question generator object.
        """
        generator: Optional[QuestionGenerator] = self._get_data(
            key=_Keys.GENERATOR, default_value=None
        )
        if generator is None:
            raise Raise.error(
                "QuestionGenerator object is not initialized",
                RuntimeError,
                self._c_name,
                currentframe(),
            )
        return generator

    @property
    def running(self) -> bool:
        """Check if the application is running.

        ### Returns:
        bool - True if running, False otherwise.
        """
        running: Optional[bool] = self._get_data(key=_Keys.RUNNING, default_value=None)
        if running is None:
            raise Raise.error(
                "Running state is not initialized",
                RuntimeError,
                self._c_name,
                currentframe(),
            )
        return running

    @running.setter
    def running(self, value: bool) -> None:
        """Set the running state of the application.

        ### Arguments:
        * value: bool - The new running state.
        """
        if not isinstance(value, bool):
            raise Raise.error(
                "Running state must be a boolean",
                TypeError,
                self._c_name,
                currentframe(),
            )
        self._set_data(key=_Keys.RUNNING, value=value)

    def _signal_handler(self, signum: int, frame) -> None:
        """Handle SIGINT (Ctrl+C) signal.

        ### Arguments:
        * signum: int - Signal number.
        * frame: frame - Current stack frame.
        """
        self.running = False
        print("\n\nInterrupted by user...")

    def _clear_screen(self) -> None:
        """Clear the terminal screen."""
        os.system("clear" if os.name == "posix" else "cls")

    def _show_banner(self) -> None:
        """Display the application banner."""
        from py_math_wizards.banner import Banner

        print(Banner.get_banner())
        print()

    def _show_greeting(self) -> None:
        """Display a random greeting message."""
        from py_math_wizards.greetings import Greetings

        print(Greetings.get_greeting())
        print()

    def _get_user_answer(self, prompt: str) -> int:
        """Get and validate user answer.

        ### Arguments:
        * prompt: str - The question prompt to display.

        ### Returns:
        int - The user's answer as an integer.

        ### Raises:
        * ValueError: If the user input is not a valid integer.
        """
        while True:
            try:
                answer = input(prompt)
                return int(answer)
            except ValueError:
                print("Please enter a whole number (integer).")
                continue
            except EOFError:
                raise Raise.error(
                    "Unexpected end of input", EOFError, self._c_name, currentframe()
                )

    def _ask_question(self) -> bool:
        """Ask a single multiplication question.

        ### Returns:
        bool - True if the user wants to continue, False otherwise.
        """
        from py_math_wizards.messages import Messages

        # Generate question
        a, b, correct_answer = self.generator.generate()
        while a in self.archive_a or b in self.archive_b:
            a, b, correct_answer = self.generator.generate()
        self.archive_a = a
        self.archive_b = b

        question = self.generator.format_question(a, b)

        # Get user answer
        try:
            user_answer = self._get_user_answer(question)
        except (EOFError, KeyboardInterrupt):
            return False

        # Check answer
        self.statistics.add_question()
        if user_answer == correct_answer:
            self.statistics.add_correct()
            print(f"✓ {Messages.get_success_message()}")
        else:
            self.statistics.add_incorrect()
            print(
                f"✗ {Messages.get_failure_message()} (Correct answer: {correct_answer})"
            )

        print()
        return True

    def run(self) -> None:
        """Run the main application loop."""
        # Display initial screen
        self._clear_screen()
        self._show_banner()
        self._show_greeting()

        # Main game loop
        while self.running:
            if not self._ask_question():
                break

        # Show final statistics
        print(self.statistics.get_report())


def main() -> None:
    """Main entry point for the application."""
    app = MathWizards()
    app.run()


if __name__ == "__main__":
    main()
