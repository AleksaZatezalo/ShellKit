from setuptools import setup, find_packages
from os import path

# Read the contents of README.md
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="shellkit",
    version="0.1.0",
    author="Aleksa Zatezalo",
    author_email="zabumaphu@gmail.com",
    description="A comprehensive security testing and exploitation framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/shellkit",
    packages=find_packages(exclude=["tests*", "examples*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Security",
        "Topic :: Security",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12.6",
    install_requires=[
        # Core HTTP and Networking
        "requests==2.31.0",
        "urllib3==2.2.0",
        "aiohttp==3.9.3",
        "beautifulsoup4==4.12.3",
        "paramiko==3.4.0",
        # Template Engines
        "Jinja2==3.1.3",
        "Mako==1.3.2",
        "tornado==6.4.0",
        # Database Connectors
        "mysql-connector-python==8.3.0",
        "psycopg2-binary==2.9.9",
        "pymongo==4.6.1",
        "SQLAlchemy==2.0.25",
        # Serialization
        "PyYAML==6.0.1",
        "msgpack==1.0.7",
        "python-snappy==0.7.1",
        # XML Processing
        "lxml==5.1.0",
        "defusedxml==0.7.1",
        # Crypto and Hashing
        "cryptography==42.0.1",
        "pycryptodome==3.20.0",
        "bcrypt==4.1.2",
        # Network Tools
        "scapy==2.5.0",
        "pyOpenSSL==24.0.0",
        "service_identity==24.1.0",
        # Command Execution
        "pypsrp==0.8.1",
        "shellingham==1.5.4",
        # Output Formatting and CLI
        "colorama==0.4.6",
        "tqdm==4.66.2",
        "click==8.1.7",
        "rich==13.7.0",
        "tabulate==0.9.0",
        # Utility Libraries
        "python-dotenv==1.0.1",
        "humanfriendly==10.0",
        "typing-extensions==4.9.0",
        # Security Specific
        "pyjwt==2.8.0",
        "oauthlib==3.2.2",
        "python-jose==3.3.0",
        # Encoder/Decoder Utilities
        "base58==2.1.1",
        "python-baseconv==1.2.2",
        "pybase62==0.5.0",
        # Web Framework Support
        "Flask==3.0.1",
        "Django==5.0.1",
        "fastapi==0.109.0",
        "uvicorn==0.27.0",
        # Progress and Status
        "alive-progress==3.1.5",
        "halo==0.0.31",
        # File Handling
        "python-magic==0.4.27",
        "filetype==1.2.0",
        # Performance Monitoring
        "psutil==5.9.8",
        "memory-profiler==0.61.0",
    ],
    extras_require={
        "dev": [
            # Testing Tools
            "pytest==8.0.0",
            "pytest-cov==4.1.0",
            "coverage==7.4.1",
            "pytest-asyncio==0.23.5",
            "pytest-mock==3.12.0",
            # Code Quality
            "black==24.1.1",
            "isort==5.13.2",
            "flake8==7.0.0",
            "mypy==1.8.0",
            "pylint==3.0.3",
            "bandit==1.7.7",
            # Documentation
            "Sphinx==7.2.6",
            "sphinx-rtd-theme==2.0.0",
            "myst-parser==2.0.0",
            "doc8==1.1.1",
            # Development Tools
            "pre-commit==3.6.0",
            "pip-tools==7.3.0",
            # Debugging
            "ipdb==0.13.13",
            "icecream==2.1.3",
        ],
    },
    entry_points={
        "console_scripts": [
            "shellkit=shellkit.cli.main:main",
            "shellkit-encode=shellkit.cli.encoders:main",
            "shellkit-shell=shellkit.cli.shells:main",
            "shellkit-scan=shellkit.cli.scanner:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "security",
        "penetration-testing",
        "vulnerability-research",
        "web-security",
        "exploit-development",
        "security-tools",
        "hacking-tools",
        "security-testing",
        "web-application-security",
        "reverse-shell",
        "web-shell",
        "payload-generation",
        "waf-bypass",
    ],
)
