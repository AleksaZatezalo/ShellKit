"""
PostgreSQL specific HTTP encoder.

Author: Aleksa Zatezalo
Date: January 2025
"""

from ..base import BaseEncoder
import urllib.parse

class PostgresHTTPEncoder(BaseEncoder):
    """Encoder for PostgreSQL specific HTTP encoding"""
    
    def encode(self, data: str) -> str:
        """
        Encode a PostgreSQL payload for HTTP transmission:
        1. Replace spaces with +
        2. Replace quotes with $$
        3. URL encode remaining special characters
        
        Args:
            data (str): PostgreSQL payload to encode
            
        Returns:
            str: Encoded payload ready for HTTP transmission
        """
        # Replace quotes with $$
        data = data.replace("'", "$$")
        
        # Replace spaces with +
        data = data.replace(" ", "+")
        
        # URL encode remaining special characters, preserving + and $
        return urllib.parse.quote(data, safe='+$')

    def decode(self, data: str) -> str:
        """
        Decode a PostgreSQL HTTP encoded payload.
        
        Args:
            data (str): Encoded payload to decode
            
        Returns:
            str: Original payload
        """
        # First decode URL encoding
        decoded = urllib.parse.unquote(data)
        
        # Replace + with spaces
        decoded = decoded.replace("+", " ")
        
        # Replace $$ with quotes
        decoded = decoded.replace("$$", "'")
        
        return decoded