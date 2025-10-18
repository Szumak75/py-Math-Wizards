"""
Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
Created: 2025-10-18

Purpose: Main application module for Math Wizards.
"""

import os
import signal
import sys
from typing import TYPE_CHECKING

from jsktoolbox.basetool import BData
from jsktoolbox.raisetool import Raise

if TYPE_CHECKING:
    from py_math_wizards.question_generator import QuestionGenerator
    from py_math_wizards.statistics import Statistics


class MathWizards(BData):
    """Main application class for Math Wizards."""

    def __init__(self) -> None:
        """Initialize MathWizards application."""
        from py_math_wizards.question_generator import QuestionGenerator
        from py_math_wizards.statistics import Statistics

        self._data["statistics"] = Statistics()
        self._data["generator"] = QuestionGenerator(0, 10)
        self._data["running"] = True

        # Setup signal handler for Ctrl+C
        signal.signal(signal.SIGINT, self._signal_handler)

    def _signal_handler(self, signum: int, frame) -> None:
        """Handle SIGINT (Ctrl+C) signal.

        ### Arguments:
        * signum: int - Signal number.
        * frame: frame - Current stack frame.
        """
        self._data["running"] = False
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
                    "Unexpected end of input",
                    EOFError,
                    self.__class__.__name__,
                    None,
                )

    def _ask_question(self) -> bool:
        """Ask a single multiplication question.

        ### Returns:
        bool - True if the user wants to continue, False otherwise.
        """
        from py_math_wizards.messages import Messages

        # Generate question
        a, b, correct_answer = self._data["generator"].generate()
        question = self._data["generator"].format_question(a, b)

        # Get user answer
        try:
            user_answer = self._get_user_answer(question)
        except (EOFError, KeyboardInterrupt):
            return False

        # Check answer
        self._data["statistics"].add_question()
        if user_answer == correct_answer:
            self._data["statistics"].add_correct()
            print(f"✓ {Messages.get_success_message()}")
        else:
            self._data["statistics"].add_incorrect()
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
        while self._data["running"]:
            if not self._ask_question():
                break

        # Show final statistics
        print(self._data["statistics"].get_report())


def main() -> None:
    """Main entry point for the application."""
    app = MathWizards()
    app.run()


if __name__ == "__main__":
    main()
