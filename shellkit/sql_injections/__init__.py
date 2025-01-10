"""
ShellKit SQL Injection Module

This module provides tools for testing and exploiting SQL injection vulnerabilities
in PostgreSQL databases, with a focus on time-based blind injection techniques.

Author: Aleksa Zatezalo
Date: January 2025
"""

from .exploiter import PostgresExploiter
from .payloads import PostgresPayloadGenerator

__version__ = '0.1.0'
__author__ = 'Aleksa Zatezalo'
__email__ = 'zabumaphu@gmail.com'

# Define public interface
__all__ = [
    'PostgresExploiter',
    'PostgresPayloadGenerator'
]

# Version information tuple
VERSION = (0, 1, 0)