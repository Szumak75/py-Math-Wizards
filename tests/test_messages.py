"""
Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
Created: 2025-10-18

Purpose: Unit tests for Messages module.
"""

import codecs
import unittest

from py_math_wizards.messages import Messages


class TestMessages(unittest.TestCase):
    """Test cases for Messages class."""

    def test_get_success_message_returns_string(self):
        """Test that get_success_message returns a string."""
        message = Messages.get_success_message()
        self.assertIsInstance(message, str)

    def test_get_success_message_is_decoded(self):
        """Test that success messages are properly decoded from ROT13."""
        message = Messages.get_success_message()
        # Message should not contain ROT13 artifacts
        self.assertTrue(len(message) > 0)
        # Check if it's different from original encoded form
        encoded = codecs.encode(message, "rot13")
        self.assertNotEqual(message, encoded)

    def test_get_failure_message_returns_string(self):
        """Test that get_failure_message returns a string."""
        message = Messages.get_failure_message()
        self.assertIsInstance(message, str)

    def test_get_failure_message_is_decoded(self):
        """Test that failure messages are properly decoded from ROT13."""
        message = Messages.get_failure_message()
        # Message should not contain ROT13 artifacts
        self.assertTrue(len(message) > 0)
        # Check if it's different from original encoded form
        encoded = codecs.encode(message, "rot13")
        self.assertNotEqual(message, encoded)

    def test_messages_are_different(self):
        """Test that multiple calls can return different messages."""
        messages = set()
        for _ in range(20):
            messages.add(Messages.get_success_message())
        # Should have at least 2 different messages after 20 tries
        self.assertGreater(len(messages), 1)


if __name__ == "__main__":
    unittest.main()
