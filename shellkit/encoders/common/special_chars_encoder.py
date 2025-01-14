"""
Special characters encoder for SQL injection and command injection.

Author: Aleksa Zatezalo
Date: January 2025
"""

from ..base import BaseEncoder


class SpecialCharsEncoder(BaseEncoder):
    """Encoder for special characters"""

    def __init__(self):
        self.sql_chars = {
            "'": "''",  # SQL quote escape
            '"': '""',  # Double quote escape
            ";": "\;",  # Semicolon escape
            "--": "\--",  # Comment escape
            "#": "\#",  # Hash escape
            "$": "\$",  # Dollar escape
        }

        self.shell_chars = {
            "&": "\&",  # Ampersand escape
            "|": "\|",  # Pipe escape
            ">": "\>",  # Greater than escape
            "<": "\<",  # Less than escape
            "`": "\`",  # Backtick escape
            "$": "\$",  # Dollar escape
            '"': '"',  # Double quote escape
            "'": "'",  # Single quote escape
            "(": "\(",  # Open parenthesis escape
            ")": "\)",  # Close parenthesis escape
            "[": "\[",  # Open bracket escape
            "]": "\]",  # Close bracket escape
            "{": "\{",  # Open brace escape
            "}": "\}",  # Close brace escape
            "*": "\*",  # Asterisk escape
            "?": "\?",  # Question mark escape
        }

    def encode(self, data: str, char_type: str = "sql") -> str:
        """
        Encode special characters based on type.

        Args:
            data (str): Data to encode
            char_type (str): Type of special characters ('sql' or 'shell')

        Returns:
            str: Encoded data
        """
        chars = self.sql_chars if char_type == "sql" else self.shell_chars

        result = data
        for char, escaped in chars.items():
            result = result.replace(char, escaped)
        return result

    def decode(self, data: str, char_type: str = "sql") -> str:
        """
        Decode escaped special characters.

        Args:
            data (str): Data to decode
            char_type (str): Type of special characters ('sql' or 'shell')

        Returns:
            str: Decoded data
        """
        chars = self.sql_chars if char_type == "sql" else self.shell_chars

        result = data
        for char, escaped in chars.items():
            result = result.replace(escaped, char)
        return result
