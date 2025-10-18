"""
Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
Created: 2025-10-18

Purpose: Greetings module for welcome messages.
"""

import codecs
from typing import List

from jsktoolbox.attribtool import NoNewAttributes


class Greetings(NoNewAttributes):
    """Container for welcome greetings."""

    # Welcome messages (ROT13 encoded)
    _GREETINGS: List[str] = [
        "Yrg'f fgneg cenpgvpvat zhygvcyvpngvba!",
        "Jrypbzr gb Zngu Jvmneqf!",
        "Ernql gb orpbzr n zngu punzcvba?",
        "Yrg'f znxr zhygvcyvpngvba sha!",
        "Gvzr gb obbfg lbhe zngu fxvyyf!",
        "Yrg'f cenpgvpr fbzr zhygvcyvpngvba gnoyr!",
        "Trg ernql sbe fbzr sha zngu punyyratrf!",
        "Yrg'f fgneg lbhe zngu nqiragher!",
        "Jrypbzr! Yrg'f cenpgvpr gbqnl!",
        "Ernql gb znfgre zhygvcyvpngvba?",
        "Gvzr gb orpbzr n zhygvcyvpngvba jvmneq!",
        "Yrg'f unir fbzr sha jvgu ahzoref!",
        "Jrypbzr gb lbhe zngu wbhearl!",
        "Ernql gb fbyir fbzr ceboyrזf?",
        "Yrg'f cenpgvpr naq vzcebir!",
    ]

    def __init__(self) -> None:
        """Initialize Greetings."""
        pass

    @classmethod
    def get_greeting(cls) -> str:
        """Get a random greeting message.

        ### Returns:
        str - A decoded greeting message.
        """
        import random

        encoded = random.choice(cls._GREETINGS)
        return codecs.decode(encoded, "rot13")
