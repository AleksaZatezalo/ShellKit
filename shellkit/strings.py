#!/usr/bin/env python3

"""
Author: Aleksa Zatezalo
Date: January 2025
Version: 1.0
Description: A set of string manipulation functions. Includes methods for removing tabs, 
            replacing carriage returns, replacing double colons, and base64 encoding input strings.
"""

import base64

def removeTabs(input_string):
    """
    Takes a string, input_string, and removes all the tabs from the string.
    The function returns the tab-less string.

    Args:
        input_string (str): The input string from which tabs are to be removed.

    Returns:
        str: A string with all tabs removed.
    """

    return input_string.replace("\t", "")

def replaceCarriageReturns(input_string):
    """
    Takes a string, input_string, and replaces all the carriage returns with a colon.
    The function returns the new string.

    Args:
        input_string (str): The input string where carriage returns need to be replaced.

    Returns:
        str: A string with carriage returns replaced by colons.
    """
    
    return input_string.replace("\n", ":")

def replaceDoubleColons(input_string):
    """
    Takes a string, input_string, and replaces all double colons ('::') with a single colon (':').
    The function returns the new string.

    Args:
        input_string (str): The input string where double colons need to be replaced.

    Returns:
        str: A string with double colons replaced by single colons.
    """

    return input_string.replace("::", ":")

def base64Encode(input_string):
    """
    Takes a string, input_string, and returns a base64 encoded version of input_string.

    Args:
        input_string (str): The input string to be base64 encoded.

    Returns:
        str: The base64 encoded version of the input string.
    """
    
    if isinstance(input_string, str):
        input_string = input_string.encode('utf-8')
    # Encode the bytes to Base64
    encoded_data = base64.b64encode(input_string)
    # Convert the encoded bytes back to a string and return
    return encoded_data.decode('utf-8')