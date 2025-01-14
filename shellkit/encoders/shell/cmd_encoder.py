"""
Windows Command Prompt encoder for shell commands.

Author: Aleksa Zatezalo
Date: January 2025
"""

from ..base import BaseEncoder


class CommandEncoder(BaseEncoder):
    """Encoder for Windows CMD commands"""

    def __init__(self):
        self.special_chars = {
            "&": "^&",
            "|": "^|",
            ">": "^>",
            "<": "^<",
            "^": "^^",
            "(": "^(",
            ")": "^)",
            "%": "%%",
        }

    def encode(self, data: str) -> str:
        """
        Encode CMD special characters.

        Args:
            data (str): Command to encode

        Returns:
            str: Encoded command
        """
        result = data
        for char, escaped in self.special_chars.items():
            result = result.replace(char, escaped)
        return result

    def decode(self, data: str) -> str:
        """
        Decode CMD special characters.

        Args:
            data (str): Encoded command

        Returns:
            str: Original command
        """
        result = data
        for char, escaped in self.special_chars.items():
            result = result.replace(escaped, char)
        return result
