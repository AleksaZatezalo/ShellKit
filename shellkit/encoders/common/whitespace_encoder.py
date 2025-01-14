"""
Whitespace encoder for WAF bypass.

Author: Aleksa Zatezalo
Date: January 2025
"""

from ..base import BaseEncoder


class WhitespaceEncoder(BaseEncoder):
    """Encoder for whitespace manipulation"""

    def __init__(self):
        self.whitespace_variants = {
            "comment": "/**/",
            "tab": "\t",
            "newline": "\n",
            "carriage": "\r",
            "url": "%20",
            "plus": "+",
            "unicode": "\u0020",
        }

    def encode(self, data: str, variant: str = "comment") -> str:
        """
        Replace spaces with specified whitespace variant.

        Args:
            data (str): Data to encode
            variant (str): Type of whitespace replacement

        Returns:
            str: Data with replaced whitespace
        """
        if variant not in self.whitespace_variants:
            raise ValueError(f"Unsupported whitespace variant: {variant}")

        return data.replace(" ", self.whitespace_variants[variant])

    def decode(self, data: str) -> str:
        """
        Decode whitespace variants back to spaces.

        Args:
            data (str): Data to decode

        Returns:
            str: Data with normalized whitespace
        """
        for variant in self.whitespace_variants.values():
            data = data.replace(variant, " ")
        return data
