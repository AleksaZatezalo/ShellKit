"""
Character encoder for basic character transformations.

Author: Aleksa Zatezalo
Date: January 2025
"""

from ..base import BaseEncoder

class CharEncoder(BaseEncoder):
    """Encoder for basic character transformations"""
    
    def html_encode(self, data: str) -> str:
        """HTML entity encode characters"""
        html_chars = {
            '<': '&lt;',
            '>': '&gt;',
            '&': '&amp;',
            '"': '&quot;',
            "'": '&#39;'
        }
        return ''.join(html_chars.get(c, c) for c in data)

    def unicode_encode(self, data: str) -> str:
        """Unicode encode characters"""
        return ''.join(f'\\u{ord(c):04x}' for c in data)

    def hex_encode(self, data: str) -> str:
        """Hex encode characters"""
        return ''.join(f'\\x{ord(c):02x}' for c in data)
        
    def encode(self, data: str, encoding_type: str = 'html') -> str:
        """
        Encode the input data using specified encoding type.
        
        Args:
            data (str): Data to encode
            encoding_type (str): Type of encoding (html, unicode, hex)
            
        Returns:
            str: Encoded data
        """
        encoders = {
            'html': self.html_encode,
            'unicode': self.unicode_encode,
            'hex': self.hex_encode
        }
        
        encoder = encoders.get(encoding_type.lower())
        if not encoder:
            raise ValueError(f"Unsupported encoding type: {encoding_type}")
            
        return encoder(data)

    def decode(self, data: str) -> str:
        """
        Decode the input data (not implemented for character encoder).
        
        Args:
            data (str): Data to decode
            
        Returns:
            str: Original data
        """
        return data  # Character encoding is typically one-way