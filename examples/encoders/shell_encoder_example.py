#!/usr/bin/env python3
"""
Shell Encoder usage examples.

Author: Aleksa Zatezalo
Date: January 2025
"""

import sys
import os

# Add shellkit to path
current_dir = os.path.dirname(os.path.abspath(__file__))
shellkit_path = os.path.abspath(os.path.join(current_dir, "../../shellkit"))
sys.path.insert(0, shellkit_path)

from shellkit.encoders.shell import CommandEncoder, PowerShellEncoder, BashEncoder


def test_cmd_encoder():
    print("Windows CMD Encoder Examples:")
    encoder = CommandEncoder()

    commands = [
        "dir & type secret.txt",
        "netstat -an > output.txt",
        "whoami && ipconfig",
    ]

    for cmd in commands:
        encoded = encoder.encode(cmd)
        print(f"\nOriginal: {cmd}")
        print(f"Encoded:  {encoded}")
    print()


def test_powershell_encoder():
    print("PowerShell Encoder Examples:")
    encoder = PowerShellEncoder()

    commands = [
        "Get-Process | Where-Object {$_.CPU -gt 50}",
        "$user = Get-ADUser -Filter * | Select-Object Name",
        'Invoke-WebRequest -Uri "http://example.com"',
    ]

    print("\nEscape Encoding:")
    for cmd in commands:
        encoded = encoder.encode(cmd, "escape")
        print(f"\nOriginal: {cmd}")
        print(f"Encoded:  {encoded}")

    print("\nBase64 Encoding:")
    encoded = encoder.encode(commands[0], "base64")
    print(f"\nOriginal: {commands[0]}")
    print(f"Encoded:  {encoded}")
    print()


def test_bash_encoder():
    print("Bash Encoder Examples:")
    encoder = BashEncoder()

    commands = [
        "cat /etc/passwd | grep root",
        'find / -name "*.txt" > files.txt',
        "ps aux | grep apache",
    ]

    print("\nEscape Encoding:")
    for cmd in commands:
        encoded = encoder.encode(cmd, "escape")
        print(f"\nOriginal: {cmd}")
        print(f"Encoded:  {encoded}")

    print("\nBase64 Encoding:")
    encoded = encoder.encode(commands[0], "base64")
    print(f"\nOriginal: {commands[0]}")
    print(f"Encoded:  {encoded}")

    print("\nHex Encoding:")
    encoded = encoder.encode(commands[0], "hex")
    print(f"\nOriginal: {commands[0]}")
    print(f"Encoded:  {encoded}")


def main():
    test_cmd_encoder()
    test_powershell_encoder()
    test_bash_encoder()


if __name__ == "__main__":
    main()
