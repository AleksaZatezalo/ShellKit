# HTTP Encoding Module Documentation

## Overview

The HTTP Encoding module in ShellKit provides various encoding techniques commonly used in web application security testing. These encoders are particularly useful for:
- Bypassing Web Application Firewalls (WAF)
- Evading Input Validation
- Testing Parameter Handling
- Payload Obfuscation

## Available Encoders

### URL Encoder
Basic URL encoding for HTTP parameters.

```python
from shellkit.encoders import URLEncoder

encoder = URLEncoder()
payload = "SELECT * FROM users"
encoded = encoder.encode(payload)  # SELECT+*+FROM+users
decoded = encoder.decode(encoded)  # SELECT * FROM users
```

### Double Encoder
Performs two passes of URL encoding, useful for bypassing certain security filters.

```python
from shellkit.encoders import DoubleEncoder

encoder = DoubleEncoder()
payload = "SELECT * FROM users"
encoded = encoder.encode(payload)  # %2553%2545%254C%2545%2543%2554...
decoded = encoder.decode(encoded)  # SELECT * FROM users

# Encode single character
char_encoded = encoder.encode_char('<')  # %253C
```

### UTF Encoder
Converts characters to their UTF-8 representation using %u encoding.

```python
from shellkit.encoders import UTFEncoder

encoder = UTFEncoder()
payload = "SELECT"
encoded = encoder.encode(payload)  # %u0053%u0045%u004C%u0045%u0043%u0054
decoded = encoder.decode(encoded)  # SELECT
```

## Use Cases

### WAF Bypass Example
```python
from shellkit.encoders import DoubleEncoder, UTFEncoder

payload = "UNION SELECT password FROM users"
double_encoder = DoubleEncoder()
utf_encoder = UTFEncoder()

# Chain encodings
stage1 = double_encoder.encode(payload)
stage2 = utf_encoder.encode(stage1)

print(f"Final encoded payload: {stage2}")
```

### Parameter Pollution Example
```python
from shellkit.encoders import URLEncoder

encoder = URLEncoder()
payload = "admin' --"
encoded = encoder.encode(payload)

url = f"http://vulnerable.com/login?user={encoded}"
```

### Encoding for Different Contexts
```python
from shellkit.encoders import URLEncoder, Base64Encoder

url_encoder = URLEncoder()
base64_encoder = Base64Encoder()

# For URL parameters
url_payload = url_encoder.encode("' OR '1'='1")

# For HTTP headers
header_payload = base64_encoder.encode("Basic admin:admin")
```

## Encoder Characteristics

### URL Encoder
- Replaces spaces with '+'
- Preserves certain safe characters
- RFC 3986 compliant
- Handles ASCII and Unicode characters

### Double Encoder
- Two passes of URL encoding
- Useful for nested contexts
- Can specify safe characters
- Includes single character encoding

### UTF Encoder
- Uses %u format
- Full Unicode support
- Useful for XSS payloads
- Can bypass certain character filters

## Common Patterns

### Chaining Encoders
```python
from shellkit.encoders import URLEncoder, Base64Encoder, UTFEncoder

def chain_encode(payload: str) -> str:
    url_encoder = URLEncoder()
    base64_encoder = Base64Encoder()
    utf_encoder = UTFEncoder()
    
    stage1 = base64_encoder.encode(payload)
    stage2 = utf_encoder.encode(stage1)
    stage3 = url_encoder.encode(stage2)
    
    return stage3
```

### Custom Safe Characters
```python
from shellkit.encoders import DoubleEncoder

encoder = DoubleEncoder()
payload = "SELECT * FROM users WHERE id='1'"
encoded = encoder.encode(payload, safe="=")  # Preserves = character
```

## Best Practices

1. **Testing Decoded Output**
   - Always verify decoded output matches input
   - Test with special characters
   - Verify in target context

2. **Security Considerations**
   - Use appropriate encoder for context
   - Consider character set restrictions
   - Test for proper decoding

3. **Performance**
   - Chain encoders efficiently
   - Cache encoder instances
   - Handle large payloads appropriately

## Troubleshooting

### Common Issues

1. **Incorrect Decoding**
   ```python
   # Problem: Multiple encodings in wrong order
   payload = "SELECT"
   encoded = utf_encoder.encode(base64_encoder.encode(payload))
   # Solution: Decode in reverse order
   decoded = base64_encoder.decode(utf_encoder.decode(encoded))
   ```

2. **Character Set Issues**
   ```python
   # Handle non-ASCII characters properly
   encoder = UTFEncoder()
   payload = "パスワード"  # Japanese for "password"
   encoded = encoder.encode(payload)
   ```

### Error Cases
- Invalid UTF-8 sequences
- Malformed URL encoding
- Incomplete multi-byte characters

## Future Enhancements

Planned features:
- HTML entity encoding
- JavaScript escape encoding
- XML entity encoding
- Automated encoding detection
- Context-aware encoding

## Contributing

To add new encoders:
1. Inherit from BaseEncoder
2. Implement encode() and decode() methods
3. Add tests for all edge cases
4. Update documentation
5. Submit a pull request