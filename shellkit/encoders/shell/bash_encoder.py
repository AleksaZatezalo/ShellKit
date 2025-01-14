"""
Bash command encoder.

Author: Aleksa Zatezalo
Date: January 2025
"""

from ..base import BaseEncoder
import base64


class BashEncoder(BaseEncoder):
    """Encoder for Bash commands"""

    def __init__(self):
        self.special_chars = {
            " ": "\\ ",
            '"': '\\"',
            "'": "\\'",
            "|": "\\|",
            "&": "\\&",
            ";": "\\;",
            "(": "\\(",
            ")": "\\)",
            "<": "\\<",
            ">": "\\>",
            "$": "\\$",
            "`": "\\`",
            "!": "\\!",
            "*": "\\*",
            "?": "\\?",
            "[": "\\[",
            "]": "\\]",
            "#": "\\#",
            "~": "\\~",
            "=": "\\=",
            "%": "\\%",
        }

    def encode(self, data: str, method: str = "escape") -> str:
        """
        Encode Bash command.

        Args:
            data (str): Command to encode
            method (str): Encoding method ('escape', 'base64', 'hex')

        Returns:
            str: Encoded command
        """
        if method == "escape":
            return self._escape_chars(data)
        elif method == "base64":
            return self._base64_encode(data)
        elif method == "hex":
            return self._hex_encode(data)
        else:
            raise ValueError(f"Unsupported encoding method: {method}")

    def decode(self, data: str, method: str = "escape") -> str:
        """
        Decode Bash command.

        Args:
            data (str): Encoded command
            method (str): Encoding method used

        Returns:
            str: Original command
        """
        if method == "escape":
            return self._unescape_chars(data)
        elif method == "base64":
            return self._base64_decode(data)
        elif method == "hex":
            return self._hex_decode(data)
        else:
            raise ValueError(f"Unsupported encoding method: {method}")

    def _escape_chars(self, data: str) -> str:
        """Escape special characters"""
        result = data
        for char, escaped in self.special_chars.items():
            result = result.replace(char, escaped)
        return result

    def _unescape_chars(self, data: str) -> str:
        """Unescape special characters"""
        result = data
        for char, escaped in self.special_chars.items():
            result = result.replace(escaped, char)
        return result

    def _base64_encode(self, data: str) -> str:
        """Base64 encode Bash command"""
        encoded = base64.b64encode(data.encode()).decode()
        return f"echo {encoded} | base64 -d | bash"

    def _base64_decode(self, data: str) -> str:
        """Base64 decode Bash command"""
        if " | base64 -d | bash" in data:
            encoded = data.split(" ")[1]
            return base64.b64decode(encoded).decode()
        return data

    def _hex_encode(self, data: str) -> str:
        """Hex encode Bash command"""
        hex_str = "".join([hex(ord(c))[2:] for c in data])
        return f"echo {hex_str} | xxd -p -r | bash"

    def _hex_decode(self, data: str) -> str:
        """Hex decode Bash command"""
        if " | xxd -p -r | bash" in data:
            hex_str = data.split(" ")[1]
            return bytes.fromhex(hex_str).decode()
        return data
