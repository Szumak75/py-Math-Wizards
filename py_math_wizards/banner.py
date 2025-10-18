"""
Author:  Jacek 'Szumak' Kotlarski --<szumak@virthost.pl>
Created: 2025-10-18

Purpose: Banner module for ASCII art display.
"""

from typing import List

from jsktoolbox.attribtool import NoNewAttributes


class Banner(NoNewAttributes):
    """ASCII banner for the application."""

    _BANNER: List[str] = [
        "  __  __       _   _       __        ___                  _     ",
        " |  \\/  | __ _| |_| |__    \\ \\      / (_)______ _ _ __ __| |___ ",
        " | |\\/| |/ _` | __| '_ \\    \\ \\ /\\ / /| |_  / _` | '__/ _` / __|",
        " | |  | | (_| | |_| | | |    \\ V  V / | |/ / (_| | | | (_| \\__ \\",
        " |_|  |_|\\__,_|\\__|_| |_|     \\_/\\_/  |_/___\\__,_|_|  \\__,_|___/",
    ]

    def __init__(self) -> None:
        """Initialize Banner."""
        pass

    @classmethod
    def get_banner(cls) -> str:
        """Get the ASCII banner.

        ### Returns:
        str - The complete banner as a string.
        """
        return "\n".join(cls._BANNER)
