"""
Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
Created: 2025-10-18

Purpose: Unit tests for QuestionGenerator module.
"""

import unittest

from py_math_wizards.question_generator import QuestionGenerator


class TestQuestionGenerator(unittest.TestCase):
    """Test cases for QuestionGenerator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.generator = QuestionGenerator(0, 10)

    def test_generate_returns_tuple(self):
        """Test that generate returns a tuple of three integers."""
        result = self.generator.generate()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
        self.assertIsInstance(result[0], int)
        self.assertIsInstance(result[1], int)
        self.assertIsInstance(result[2], int)

    def test_generate_correct_answer(self):
        """Test that the generated answer is correct."""
        a, b, answer = self.generator.generate()
        self.assertEqual(answer, a * b)

    def test_generate_within_range(self):
        """Test that generated numbers are within specified range."""
        for _ in range(20):
            a, b, _ = self.generator.generate()
            self.assertGreaterEqual(a, 0)
            self.assertLessEqual(a, 10)
            self.assertGreaterEqual(b, 0)
            self.assertLessEqual(b, 10)

    def test_custom_range(self):
        """Test generator with custom range."""
        generator = QuestionGenerator(5, 8)
        for _ in range(20):
            a, b, _ = generator.generate()
            self.assertGreaterEqual(a, 5)
            self.assertLessEqual(a, 8)
            self.assertGreaterEqual(b, 5)
            self.assertLessEqual(b, 8)

    def test_format_question(self):
        """Test question formatting."""
        question = self.generator.format_question(5, 3)
        self.assertIsInstance(question, str)
        self.assertIn("5", question)
        self.assertIn("3", question)
        self.assertIn("×", question)
        self.assertIn("=", question)

    def test_format_question_various_inputs(self):
        """Test formatting with various inputs."""
        test_cases = [(0, 0), (1, 1), (10, 10), (5, 7)]
        for a, b in test_cases:
            question = self.generator.format_question(a, b)
            self.assertIn(str(a), question)
            self.assertIn(str(b), question)


if __name__ == "__main__":
    unittest.main()
