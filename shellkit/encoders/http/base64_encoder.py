"""
Base64 encoder for payload encoding.

Author: Aleksa Zatezalo
Date: January 2025
"""

from .base import BaseEncoder
import base64


class Base64Encoder(BaseEncoder):
    """Encoder for Base64 encoding payloads"""

    def encode(self, data: str) -> str:
        """
        Base64 encode a string.

        Args:
            data (str): Data to encode

        Returns:
            str: Base64 encoded string
        """
        return base64.b64encode(data.encode()).decode()

    def decode(self, data: str) -> str:
        """
        Decode a Base64 encoded string.

        Args:
            data (str): Base64 encoded data to decode

        Returns:
            str: Decoded string
        """
        return base64.b64decode(data.encode()).decode()
