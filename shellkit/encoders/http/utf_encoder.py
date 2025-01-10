"""
UTF encoder for payload encoding.

Author: Aleksa Zatezalo
Date: January 2025
"""

from .base import BaseEncoder

class UTFEncoder(BaseEncoder):
    """Encoder for UTF encoding payloads"""
    
    def encode(self, data: str) -> str:
        """
        UTF encode a string, converting characters to their UTF-8 representation.
        
        Args:
            data (str): Data to encode
            
        Returns:
            str: UTF encoded string
        """
        encoded = ""
        for char in data:
            encoded += f"%u{ord(char):04x}"
        return encoded

    def decode(self, data: str) -> str:
        """
        Decode a UTF encoded string.
        
        Args:
            data (str): UTF encoded data to decode
            
        Returns:
            str: Decoded string
        """
        decoded = ""
        chunks = data.split("%u")
        for chunk in chunks[1:]:  # Skip first empty chunk
            if len(chunk) >= 4:
                decoded += chr(int(chunk[:4], 16))
        return decoded