# 🛡️ ShellKit

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</div>

ShellKit is an open-source, Python-based framework designed specifically for rapid development, testing, and automation of web application exploits. Built with the needs of security researchers, penetration testers, and CTF enthusiasts in mind, ShellKit provides a powerful set of tools focused on exploiting common web vulnerabilities like SQL injection, XSS, RCE (Remote Code Execution), file inclusion, and command injection.

## 🚀 Features

### Core Capabilities
* **Vulnerability Testing & Exploitation**
  - SQL Injection (Error-based, Boolean-based, Time-based)
  - Cross-Site Scripting (XSS)
  - Server-Side Template Injection (SSTI)
  - Insecure Deserialization
  - Server-Side Request Forgery (SSRF)
  - Command Injection
  - Prototype Pollution
  - WAF Bypass Techniques

### Advanced Tools
* **Shell Generation & Management**
  - Reverse Shell Generator (Multi-language support)
  - Web Shell Templates
  - Bind Shell Creator
  - Custom Shell Encoding

* **Payload Engineering**
  - Advanced Encoding/Decoding
  - HTTP Request Manipulation
  - Character Set Handlers
  - WAF Evasion Techniques

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/shellkit.git
cd shellkit

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```

## 🎮 Quick Start

```python
from shellkit.sql_injection import SQLInjector
from shellkit.shells import ReverseShellGenerator
from shellkit.encoders import Base64ShellEncoder

# SQL Injection Example
injector = SQLInjector()
result = injector.test_injection(
    url="http://target.com/vulnerable.php",
    parameter="id",
    technique="boolean"
)

# Generate an Encoded Reverse Shell
generator = ReverseShellGenerator()
encoder = Base64ShellEncoder()

shell = generator.generate(
    language="python",
    ip="10.10.10.10",
    port=4444
)

encoded_shell = encoder.encode(shell)
```

## 📚 Documentation

Detailed documentation is available at [docs/](docs/).

## 🔬 Supported Vulnerabilities

| Vulnerability Type | Status | Description |
|-------------------|---------|-------------|
| SQL Injection | ✅ | Error, Boolean, Time-based methods |
| XSS | ✅ | Reflected, Stored, DOM-based |
| SSTI | ✅ | Multiple template engine support |
| Deserialization | ✅ | Python, PHP, Java formats |
| SSRF | ✅ | Internal/External resource access |
| Command Injection | ✅ | OS command execution |
| Prototype Pollution | ✅ | JavaScript object manipulation |
| WAF Bypass | ✅ | Various evasion techniques |

## 🤝 Contributing

We welcome contributions! Please see our Contributing Guidelines for details. Key points:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🔒 Security

- All exploits are designed for authorized testing only
- Review target scope and permissions before testing
- Follow responsible disclosure practices

## 🙏 Acknowledgments

- Contributors & community members
- Open source security tools that inspired this project
- Security researchers who share their knowledge

## 📞 Contact & Support

- Submit bug reports and feature requests via [GitHub Issues](https://github.com/AleksaZatezalo/shellkit/issues)
- Follow the project creator for updates on [Twitter](https://twitter.com/ZatezaloAleksa)

## ⚠️ Disclaimer

ShellKit is intended for legal security testing only. Users are responsible for obtaining proper authorization before testing any systems. The developers assume no liability for misuse or damage caused by this tool.

---

<div align="center">
Made with ❤️ by the Security Research Community
</div>

## Donation Link

If you have benefited from this project and use Monero please consider donanting to the following address:
47RoH3K4j8STLSh8ZQ2vUXZdh7GTK6dBy7uEBopegzkp6kK4fBrznkKjE3doTamn3W7A5DHbWXNdjaz2nbZmSmAk8X19ezQ