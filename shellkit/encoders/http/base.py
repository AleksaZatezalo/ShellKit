"""
Base encoder class for ShellKit encoders.

Author: Aleksa Zatezalo
Date: January 2025
"""

from abc import ABC, abstractmethod

class BaseEncoder(ABC):
    """Base class for all encoders in ShellKit"""
    
    @abstractmethod
    def encode(self, data: str) -> str:
        """
        Encode the input data.
        
        Args:
            data (str): Data to encode
            
        Returns:
            str: Encoded data
        """
        pass

    @abstractmethod
    def decode(self, data: str) -> str:
        """
        Decode the input data.
        
        Args:
            data (str): Data to decode
            
        Returns:
            str: Decoded data
        """
        pass