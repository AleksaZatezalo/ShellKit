
"""
PowerShell command encoder.

Author: Aleksa Zatezalo
Date: January 2025
"""

from ..base import BaseEncoder
import base64

class PowerShellEncoder(BaseEncoder):
    """Encoder for PowerShell commands"""
    
    def __init__(self):
        self.special_chars = {
            '"': '`"',
            "'": "`'",
            '$': '`$',
            '`': '``',
            '#': '`#',
            '|': '`|',
            '>': '`>',
            '<': '`<',
            '(': '`(',
            ')': '`)',
            '[': '`[',
            ']': '`]',
            '{': '`{',
            '}': '`}'
        }

    def encode(self, data: str, method: str = 'escape') -> str:
        """
        Encode PowerShell command.
        
        Args:
            data (str): Command to encode
            method (str): Encoding method ('escape', 'base64', 'compressed')
            
        Returns:
            str: Encoded command
        """
        if method == 'escape':
            return self._escape_chars(data)
        elif method == 'base64':
            return self._base64_encode(data)
        elif method == 'compressed':
            return self._compress_encode(data)
        else:
            raise ValueError(f"Unsupported encoding method: {method}")

    def decode(self, data: str, method: str = 'escape') -> str:
        """
        Decode PowerShell command.
        
        Args:
            data (str): Encoded command
            method (str): Encoding method used
            
        Returns:
            str: Original command
        """
        if method == 'escape':
            return self._unescape_chars(data)
        elif method == 'base64':
            return self._base64_decode(data)
        elif method == 'compressed':
            return self._compress_decode(data)
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
        """Base64 encode PowerShell command"""
        encoded = base64.b64encode(data.encode('utf-16le')).decode()
        return f"powershell -enc {encoded}"

    def _base64_decode(self, data: str) -> str:
        """Base64 decode PowerShell command"""
        if data.startswith("powershell -enc "):
            data = data[16:]
        return base64.b64decode(data).decode('utf-16le')

    def _compress_encode(self, data: str) -> str:
        """Compress and encode PowerShell command"""
        # Implementation for compressed PowerShell commands
        raise NotImplementedError("Compression encoding not implemented")

    def _compress_decode(self, data: str) -> str:
        """Decompress and decode PowerShell command"""
        # Implementation for compressed PowerShell commands
        raise NotImplementedError("Compression decoding not implemented")