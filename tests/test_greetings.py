"""
Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
Created: 2025-10-18

Purpose: Unit tests for Greetings module.
"""

import codecs
import unittest

from py_math_wizards.greetings import Greetings


class TestGreetings(unittest.TestCase):
    """Test cases for Greetings class."""

    def test_get_greeting_returns_string(self) -> None:
        """Test that get_greeting returns a string."""
        greeting: str = Greetings.get_greeting()
        self.assertIsInstance(greeting, str)

    def test_get_greeting_is_decoded(self) -> None:
        """Test that greetings are properly decoded from ROT13."""
        greeting: str = Greetings.get_greeting()
        # Greeting should not contain ROT13 artifacts
        self.assertTrue(len(greeting) > 0)
        # Check if it's different from original encoded form
        encoded: str = codecs.encode(greeting, "rot13")
        self.assertNotEqual(greeting, encoded)

    def test_greetings_are_different(self) -> None:
        """Test that multiple calls can return different greetings."""
        greetings: set[str] = set()
        for _ in range(20):
            greetings.add(Greetings.get_greeting())
        # Should have at least 2 different greetings after 20 tries
        self.assertGreater(len(greetings), 1)


if __name__ == "__main__":
    unittest.main()
