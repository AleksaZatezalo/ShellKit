# Common Encoding Guide

## Overview
Common encoding patterns are essential for security testing and payload generation. This module provides fundamental encoding techniques used across various security testing scenarios.

## Character Encoder

The character encoder provides basic character transformations commonly used in security testing.

### HTML Entity Encoding
```python
from shellkit.encoders.common import CharEncoder

encoder = CharEncoder()

# Basic HTML encoding
html_encoded = encoder.encode('<script>', 'html')
# Result: &lt;script&gt;

# Encoding quotes
html_encoded = encoder.encode('alert("XSS")', 'html')
# Result: alert(&quot;XSS&quot;)
```

### Unicode Encoding
```python
# Unicode encoding
unicode_encoded = encoder.encode('<script>', 'unicode')
# Result: \u003cscript\u003e

# Mixed character encoding
unicode_encoded = encoder.encode('SELECT', 'unicode')
# Result: \u0053\u0045\u004c\u0045\u0043\u0054
```

### Hex Encoding
```python
# Hex encoding
hex_encoded = encoder.encode('<script>', 'hex')
# Result: \x3cscript\x3e
```

## Whitespace Encoder

The whitespace encoder handles different whitespace representations for SQL injection and other attacks.

### SQL Comment Style
```python
from shellkit.encoders.common import WhitespaceEncoder

encoder = WhitespaceEncoder()

# Using comments
sql = encoder.encode("SELECT * FROM users", 'comment')
# Result: SELECT/**/*/**/FROM/**/users

# Using tabs
sql = encoder.encode("SELECT * FROM users", 'tab')
# Result: SELECT    *   FROM    users
```

### URL Style
```python
# URL encoding spaces
sql = encoder.encode("SELECT * FROM users", 'url')
# Result: SELECT%20*%20FROM%20users
```

## Special Characters Encoder

The special characters encoder handles escaping of special characters for different contexts.

### SQL Special Characters
```python
from shellkit.encoders.common import SpecialCharsEncoder

encoder = SpecialCharsEncoder()

# Handling SQL quotes
sql = encoder.encode("O'Reilly", 'sql')
# Result: O''Reilly

# Handling SQL commands
sql = encoder.encode("SELECT;DROP TABLE users", 'sql')
# Result: SELECT\;DROP TABLE users
```

### Shell Special Characters
```python
# Escaping shell characters
cmd = encoder.encode("cat file.txt | grep 'pattern'", 'shell')
# Result: cat file.txt \| grep \'pattern\'

# Handling command injection
cmd = encoder.encode("ls && cat /etc/passwd", 'shell')
# Result: ls \&\& cat /etc/passwd
```

## Common Use Cases

### Web Application Testing
```python
# XSS Payload
xss = '<script>alert("XSS")</script>'
html_safe = char_encoder.encode(xss, 'html')
unicode_safe = char_encoder.encode(xss, 'unicode')

# SQL Injection
sql = "' OR '1'='1"
sql_safe = special_chars_encoder.encode(sql, 'sql')
```

### Command Injection
```python
# Basic command injection
cmd = "cat /etc/passwd | grep root"
shell_safe = special_chars_encoder.encode(cmd, 'shell')

# Multiple commands
cmd = "ls; cat /etc/shadow"
shell_safe = special_chars_encoder.encode(cmd, 'shell')
```

### SQL Query Building
```python
# Building complex queries
query = "SELECT * FROM users WHERE name = 'admin'"
encoded = whitespace_encoder.encode(query, 'comment')
safe_query = special_chars_encoder.encode(encoded, 'sql')
```

## Best Practices

1. Character Encoding
   - Use HTML encoding for web content
   - Use Unicode encoding for bypass attempts
   - Use hex encoding for binary data

2. Whitespace Handling
   - Use comment style for SQL injection
   - Use URL encoding for HTTP parameters
   - Consider multiple whitespace variants

3. Special Characters
   - Always escape user input
   - Use context-appropriate escaping
   - Consider multiple layers of escaping

## Common Patterns

### Multiple Encoding Layers
```python
# Layer 1: Special characters
stage1 = special_chars_encoder.encode(payload, 'sql')

# Layer 2: Whitespace
stage2 = whitespace_encoder.encode(stage1, 'comment')

# Layer 3: Character encoding
stage3 = char_encoder.encode(stage2, 'hex')
```

### Context-Specific Encoding
```python
# Web context
web_payload = char_encoder.encode(payload, 'html')

# SQL context
sql_payload = special_chars_encoder.encode(payload, 'sql')

# Shell context
shell_payload = special_chars_encoder.encode(payload, 'shell')
```

## Security Considerations

1. Input Validation
   - Always validate input before encoding
   - Consider character set restrictions
   - Handle encoding errors gracefully

2. Output Encoding
   - Use context-appropriate encoding
   - Consider multiple encoding layers
   - Test encoded output thoroughly

3. Bypass Detection
   - Be aware of common bypass techniques
   - Test multiple encoding combinations
   - Consider security control limitations

## Testing Guidelines

1. Test each encoder individually
2. Verify encoding/decoding cycles
3. Test with different character sets
4. Test with malicious input
5. Verify output in target context

## Error Handling
```python
try:
    encoded = encoder.encode(payload, 'invalid_type')
except ValueError as e:
    print(f"Encoding error: {e}")
```

## Performance Considerations

1. Use appropriate encoding methods
2. Cache frequently used encodings
3. Consider input size limitations
4. Test with large inputs
5. Monitor encoding overhead
```

Would you like me to:
1. Add more examples?
2. Include more security considerations?
3. Add more use cases?
4. Add troubleshooting guide?
