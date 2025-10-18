"""
Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
Created: 2025-10-18

Purpose: Question generator module for multiplication problems.
"""

import random
from typing import Tuple

from jsktoolbox.basetool import BData
from jsktoolbox.attribtool import ReadOnlyClass


class _Keys(object, metaclass=ReadOnlyClass):
    """Keys class for internal purpose only."""

    MIN = "min"
    MAX = "max"


class QuestionGenerator(BData):
    """Generator for multiplication questions."""

    def __init__(self, min_value: int = 0, max_value: int = 10) -> None:
        """Initialize QuestionGenerator.

        ### Arguments:
        * min_value: int - Minimum value for operands (default: 0).
        * max_value: int - Maximum value for operands (default: 10).
        """
        self._data[_Keys.MIN] = min_value
        self._data[_Keys.MAX] = max_value

    def generate(self) -> Tuple[int, int, int]:
        """Generate a new multiplication question.

        ### Returns:
        Tuple[int, int, int] - (first_operand, second_operand, correct_answer).
        """
        a = random.randint(self._data[_Keys.MIN], self._data[_Keys.MAX])
        b = random.randint(self._data[_Keys.MIN], self._data[_Keys.MAX])
        answer = a * b
        return (a, b, answer)

    def format_question(self, a: int, b: int) -> str:
        """Format a question for display.

        ### Arguments:
        * a: int - First operand.
        * b: int - Second operand.

        ### Returns:
        str - Formatted question string.
        """
        return f"{a} × {b} = "
