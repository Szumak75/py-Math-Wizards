"""
Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
Created: 2025-10-18

Purpose: Unit tests for Statistics module.
"""

import unittest

from py_math_wizards.statistics import Statistics


class TestStatistics(unittest.TestCase):
    """Test cases for Statistics class."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        self.stats = Statistics()

    def test_initial_values(self) -> None:
        """Test that statistics are initialized to zero."""
        self.assertEqual(self.stats.total_questions, 0)
        self.assertEqual(self.stats.correct_answers, 0)
        self.assertEqual(self.stats.incorrect_answers, 0)
        self.assertEqual(self.stats.success_rate, 0.0)

    def test_add_question(self) -> None:
        """Test adding questions."""
        self.stats.add_question()
        self.assertEqual(self.stats.total_questions, 1)
        self.stats.add_question()
        self.assertEqual(self.stats.total_questions, 2)

    def test_add_correct(self) -> None:
        """Test adding correct answers."""
        self.stats.add_correct()
        self.assertEqual(self.stats.correct_answers, 1)
        self.stats.add_correct()
        self.assertEqual(self.stats.correct_answers, 2)

    def test_add_incorrect(self) -> None:
        """Test adding incorrect answers."""
        self.stats.add_incorrect()
        self.assertEqual(self.stats.incorrect_answers, 1)
        self.stats.add_incorrect()
        self.assertEqual(self.stats.incorrect_answers, 2)

    def test_success_rate_calculation(self) -> None:
        """Test success rate calculation."""
        # Add 3 questions: 2 correct, 1 incorrect
        self.stats.add_question()
        self.stats.add_correct()
        self.stats.add_question()
        self.stats.add_correct()
        self.stats.add_question()
        self.stats.add_incorrect()

        expected_rate: float = (2 / 3) * 100
        self.assertAlmostEqual(self.stats.success_rate, expected_rate, places=1)

    def test_success_rate_100_percent(self) -> None:
        """Test success rate with all correct answers."""
        self.stats.add_question()
        self.stats.add_correct()
        self.stats.add_question()
        self.stats.add_correct()

        self.assertEqual(self.stats.success_rate, 100.0)

    def test_success_rate_0_percent(self) -> None:
        """Test success rate with all incorrect answers."""
        self.stats.add_question()
        self.stats.add_incorrect()
        self.stats.add_question()
        self.stats.add_incorrect()

        self.assertEqual(self.stats.success_rate, 0.0)

    def test_get_report(self) -> None:
        """Test report generation."""
        self.stats.add_question()
        self.stats.add_correct()
        report: str = self.stats.get_report()

        self.assertIsInstance(report, str)
        self.assertIn("SESSION STATISTICS", report)
        self.assertIn("Total questions:", report)
        self.assertIn("Correct answers:", report)
        self.assertIn("Incorrect answers:", report)
        self.assertIn("Success rate:", report)


if __name__ == "__main__":
    unittest.main()
