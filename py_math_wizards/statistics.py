"""
Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
Created: 2025-10-18

Purpose: Statistics module for tracking game statistics.
"""

from jsktoolbox.basetool import BData


class Statistics(BData):
    """Game statistics tracker."""

    def __init__(self) -> None:
        """Initialize Statistics."""
        self._data["total_questions"] = 0
        self._data["correct_answers"] = 0
        self._data["incorrect_answers"] = 0

    def add_question(self) -> None:
        """Increment total questions counter."""
        self._data["total_questions"] += 1

    def add_correct(self) -> None:
        """Increment correct answers counter."""
        self._data["correct_answers"] += 1

    def add_incorrect(self) -> None:
        """Increment incorrect answers counter."""
        self._data["incorrect_answers"] += 1

    @property
    def total_questions(self) -> int:
        """Get total number of questions.

        ### Returns:
        int - Total questions asked.
        """
        return self._data["total_questions"]

    @property
    def correct_answers(self) -> int:
        """Get number of correct answers.

        ### Returns:
        int - Number of correct answers.
        """
        return self._data["correct_answers"]

    @property
    def incorrect_answers(self) -> int:
        """Get number of incorrect answers.

        ### Returns:
        int - Number of incorrect answers.
        """
        return self._data["incorrect_answers"]

    @property
    def success_rate(self) -> float:
        """Calculate success rate as percentage.

        ### Returns:
        float - Success rate as percentage (0-100).
        """
        if self.total_questions == 0:
            return 0.0
        return (self.correct_answers / self.total_questions) * 100

    def get_report(self) -> str:
        """Generate a statistics report.

        ### Returns:
        str - Formatted statistics report.
        """
        report = "\n" + "=" * 50 + "\n"
        report += "              SESSION STATISTICS\n"
        report += "=" * 50 + "\n"
        report += f"Total questions:    {self.total_questions}\n"
        report += f"Correct answers:    {self.correct_answers}\n"
        report += f"Incorrect answers:  {self.incorrect_answers}\n"
        report += f"Success rate:       {self.success_rate:.1f}%\n"
        report += "=" * 50 + "\n"
        return report
