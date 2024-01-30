#!/usr/bin/python3
""" script contain validUTF8 function"""


def validUTF8(data):
    """method that determines if a given data
    set represents a valid UTF-8 encoding"""

    try:
        _ = bytearray(data).decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
