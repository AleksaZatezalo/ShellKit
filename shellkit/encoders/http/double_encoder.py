"""
Double encoder for payload encoding.

Author: Aleksa Zatezalo
Date: January 2025
"""

from .base import BaseEncoder
import urllib.parse

class DoubleEncoder(BaseEncoder):
    """Encoder for double-encoding payloads"""
    
    def encode(self, data: str, safe: str = '') -> str:
        """
        Double URL encode a string.
        
        Args:
            data (str): Data to encode
            safe (str): Characters to leave unencoded
            
        Returns:
            str: Double URL encoded string
        """
        # First encoding
        first_pass = urllib.parse.quote(data, safe=safe)
        # Second encoding
        return urllib.parse.quote(first_pass, safe=safe)

    def decode(self, data: str) -> str:
        """
        Decode a double URL encoded string.
        
        Args:
            data (str): Double encoded data to decode
            
        Returns:
            str: Decoded string
        """
        # First decoding
        first_pass = urllib.parse.unquote(data)
        # Second decoding
        return urllib.parse.unquote(first_pass)

    def encode_char(self, char: str) -> str:
        """
        Double encode a single character.
        
        Args:
            char (str): Single character to encode
            
        Returns:
            str: Double encoded character
        """
        if len(char) != 1:
            raise ValueError("encode_char expects a single character")
        return self.encode(char)
