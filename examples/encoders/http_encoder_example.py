"""
HTTP Encoder usage examples.

Author: Aleksa Zatezalo
Date: January 2025
"""

import sys
import os

# Add shellkit to path
current_dir = os.path.dirname(os.path.abspath(__file__))
shellkit_path = os.path.abspath(os.path.join(current_dir, '../../shellkit'))
sys.path.insert(0, shellkit_path)

from shellkit.encoders.http import HTTPEncoder

def main():
    encoder = HTTPEncoder()
    
    # Basic URL encoding
    print("Basic URL Encoding:")
    payload = "select * from users where id = '1'"
    encoded = encoder.encode(payload, 'url')
    print(f"Original: {payload}")
    print(f"Encoded:  {encoded}\n")
    
    # Double encoding
    print("Double URL Encoding:")
    encoded = encoder.encode(payload, 'double')
    print(f"Original: {payload}")
    print(f"Encoded:  {encoded}\n")
    
    # Form encoding
    print("Form Encoding:")
    form_data = "username=admin&password=secret"
    encoded = encoder.encode(form_data, 'form')
    print(f"Original: {form_data}")
    print(f"Encoded:  {encoded}\n")
    
    # Parameter encoding
    print("Parameter Encoding:")
    params = {
        'query': 'SELECT * FROM users',
        'filter': 'admin',
        'limit': '10'
    }
    encoded = encoder.encode_params(params)
    print(f"Original: {params}")
    print(f"Encoded:  {encoded}\n")
    
    # Header encoding
    print("Header Encoding:")
    headers = {
        'User-Agent': 'Custom Browser/1.0',
        'X-Forwarded-For': '127.0.0.1'
    }
    encoded = encoder.encode_headers(headers)
    print(f"Original: {headers}")
    print(f"Encoded:  {encoded}\n")
    
    # Path encoding
    print("Path Encoding:")
    path = "/path/to/file with spaces.txt"
    encoded = encoder.normalize_path(path)
    print(f"Original: {path}")
    print(f"Encoded:  {encoded}")

if __name__ == "__main__":
    main()