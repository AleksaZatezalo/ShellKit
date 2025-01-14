# Contributing to ShellKit

## Testing Your Changes

### Test Bench Overview
ShellKit includes a comprehensive test bench for validating encoders and ensuring compatibility across different scenarios. The test bench is located in the `tests/` directory.

### Setting Up the Test Environment
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install test requirements:
```bash
pip install -r requirements-dev.txt
```

### Running the Test Bench

#### Full Test Suite
Run all tests:
```bash
python -m pytest tests/
```

#### Testing Specific Encoders
Test individual encoder modules:
```bash
# Test URL encoder
python -m pytest tests/test_encoders/test_url_encoder.py

# Test PostgreSQL encoder
python -m pytest tests/test_encoders/test_postgres_encoder.py
```

#### Testing with Verbose Output
For detailed test information:
```bash
python -m pytest -v tests/
```

### Adding New Tests

1. For new encoders, create a test file in `tests/test_encoders/`:
```python
# tests/test_encoders/test_new_encoder.py
import pytest
from shellkit.encoders import NewEncoder

def test_new_encoder_basic():
    encoder = NewEncoder()
    assert encoder.encode("test") == "expected_result"
```

2. For new vulnerability modules, create a test file in appropriate directory:
```python
# tests/test_sql_injection/test_new_feature.py
import pytest
from shellkit.sql_injection import NewFeature

def test_new_feature():
    feature = NewFeature()
    assert feature.run() == expected_result
```

### Test Guidelines
1. Each new feature must include tests
2. Tests should cover:
   - Basic functionality
   - Edge cases
   - Error conditions
   - Input validation
   - Special character handling

### Running Test Coverage
To check test coverage:
```bash
python -m pytest --cov=shellkit tests/

# For detailed coverage report
python -m pytest --cov=shellkit --cov-report=html tests/
```

### Continuous Integration
Tests are automatically run on:
- Pull request creation
- Push to main branch
- Daily scheduled runs

### Common Test Scenarios
Ensure your changes pass these common test scenarios:
1. Input validation tests
2. Character encoding tests
3. Edge case handling
4. Error condition tests
5. Integration tests

### Test Bench Structure
```
tests/
├── __init__.py
├── conftest.py
├── test_encoders/
│   ├── __init__.py
│   ├── test_url_encoder.py
│   ├── test_postgres_encoder.py
│   └── test_base64_encoder.py
├── test_sql_injection/
│   ├── __init__.py
│   └── test_exploiter.py
└── test_utils/
    ├── __init__.py
    └── test_helpers.py
```

### Before Submitting Changes
1. Run the full test suite
2. Check test coverage
3. Add tests for new features
4. Update test documentation
5. Verify all CI checks pass

### Debug Tests
To run tests with debug information:
```bash
python -m pytest -v --pdb tests/
```

### Test Requirements
Ensure all test dependencies are listed in `requirements-dev.txt`:
```
pytest==8.0.0
pytest-cov==4.1.0
pytest-mock==3.12.0
coverage==7.4.1
```

### Best Practices
1. Write clear test names
2. Use descriptive assertions
3. Group related tests
4. Mock external dependencies
5. Keep tests independent


## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming language
* Being respectful
* Accepting constructive criticism

Examples of unacceptable behavior by participants include:

* The use of unwelcome sexual attention or advances
* Insulting or derogatory comments, and personal or political attacks
* Publishing others' private information, such as a physical or electronic
  address

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/
