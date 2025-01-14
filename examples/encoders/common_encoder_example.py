#!/usr/bin/env python3
"""
Common Encoders usage examples.

Author: Aleksa Zatezalo
Date: January 2025
"""

import sys
import os

# Add shellkit to path
current_dir = os.path.dirname(os.path.abspath(__file__))
shellkit_path = os.path.abspath(os.path.join(current_dir, '../../shellkit'))
sys.path.insert(0, shellkit_path)

from shellkit.encoders.common import CharEncoder, WhitespaceEncoder, SpecialCharsEncoder

def test_char_encoder():
    print("Character Encoder Examples:")
    encoder = CharEncoder()
    
    test_string = '<script>alert("XSS")</script>'
    
    print("\nHTML Encoding:")
    encoded = encoder.encode(test_string, 'html')
    print(f"Original: {test_string}")
    print(f"Encoded:  {encoded}")
    
    print("\nUnicode Encoding:")
    encoded = encoder.encode(test_string, 'unicode')
    print(f"Original: {test_string}")
    print(f"Encoded:  {encoded}")
    
    print("\nHex Encoding:")
    encoded = encoder.encode(test_string, 'hex')
    print(f"Original: {test_string}")
    print(f"Encoded:  {encoded}")
    print()

def test_whitespace_encoder():
    print("Whitespace Encoder Examples:")
    encoder = WhitespaceEncoder()
    
    sql_query = "SELECT * FROM users WHERE name = 'admin'"
    
    print("\nComment Style:")
    encoded = encoder.encode(sql_query, 'comment')
    print(f"Original: {sql_query}")
    print(f"Encoded:  {encoded}")
    
    print("\nURL Style:")
    encoded = encoder.encode(sql_query, 'url')
    print(f"Original: {sql_query}")
    print(f"Encoded:  {encoded}")
    
    print("\nTab Style:")
    encoded = encoder.encode(sql_query, 'tab')
    print(f"Original: {sql_query}")
    print(f"Encoded:  {encoded}")
    print()

def test_special_chars_encoder():
    print("Special Characters Encoder Examples:")
    encoder = SpecialCharsEncoder()
    
    # SQL examples
    sql_query = "SELECT * FROM users WHERE name = 'O'Connor'"
    print("\nSQL Special Characters:")
    encoded = encoder.encode(sql_query, 'sql')
    print(f"Original: {sql_query}")
    print(f"Encoded:  {encoded}")
    
    # Shell examples
    shell_command = "cat file.txt | grep 'pattern' > output.txt"
    print("\nShell Special Characters:")
    encoded = encoder.encode(shell_command, 'shell')
    print(f"Original: {shell_command}")
    print(f"Encoded:  {encoded}")
    print()

def main():
    test_char_encoder()
    test_whitespace_encoder()
    test_special_chars_encoder()

if __name__ == "__main__":
    main()