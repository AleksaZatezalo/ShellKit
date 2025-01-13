"""
URL encoder for HTTP payloads.

Author: Aleksa Zatezalo
Date: January 2025
"""

import urllib.parse


class URLEncoder:
    """Encoder for URL encoding SQL payloads"""

    def encode(self, data: str) -> str:
        """
        URL encode a string, replacing spaces with plus signs and encoding special characters.

        Args:
            data (str): SQL payload to encode

        Returns:
            str: URL encoded payload
        """
        # First, handle spaces to pluses
        data = data.replace(" ", "+")

        # Encode special characters
        encoded = urllib.parse.quote(data, safe="+")

        return encoded

    def decode(self, data: str) -> str:
        """
        Decode a URL encoded string.

        Args:
            data (str): Encoded data to decode

        Returns:
            str: Decoded string
        """
        # First decode the percent encodings
        decoded = urllib.parse.unquote(data)

        # Then replace plus signs with spaces
        decoded = decoded.replace("+", " ")

        return decoded
