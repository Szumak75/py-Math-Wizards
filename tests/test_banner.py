"""
Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
Created: 2025-10-18

Purpose: Unit tests for Banner module.
"""

import unittest

from typing import List
from py_math_wizards.banner import Banner


class TestBanner(unittest.TestCase):
    """Test cases for Banner class."""

    def test_get_banner_returns_string(self) -> None:
        """Test that get_banner returns a string."""
        banner: str = Banner.get_banner()
        self.assertIsInstance(banner, str)

    def test_banner_not_empty(self) -> None:
        """Test that banner is not empty."""
        banner: str = Banner.get_banner()
        self.assertTrue(len(banner) > 0)

    def test_banner_contains_newlines(self) -> None:
        """Test that banner contains multiple lines."""
        banner: str = Banner.get_banner()
        self.assertIn("\n", banner)
        lines: List[str] = banner.split("\n")
        self.assertGreater(len(lines), 1)

    def test_banner_contains_text(self) -> None:
        """Test that banner contains expected text patterns."""
        banner: str = Banner.get_banner()
        # Should contain some ASCII art characters
        self.assertTrue(any(char in banner for char in ["|", "_", "/", "\\"]))


if __name__ == "__main__":
    unittest.main()
