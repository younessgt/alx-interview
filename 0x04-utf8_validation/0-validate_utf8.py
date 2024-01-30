#!/usr/bin/python3
""" script contain validUTF8 function"""


def validUTF8(data):
    """method that determines if a given data
    set represents a valid UTF-8 encoding"""

    """first solution """
    """ try:
        _ = bytearray(data).decode('utf-8')
        return True
    except Exception:
        return False """

    """second solution using bitwise operator"""
    first_bit = 1 << 7
    second_bit = 1 << 6
    count_bytes = 0

    for byte in data:
        mask = 1 << 7

        if count_bytes == 0:

            if byte & mask == 0:
                continue
            for i in range(5):
                if byte & mask >> i:
                    count_bytes += 1
                else:
                    break
            if count_bytes == 1 or count_bytes > 4 or byte > 255:
                return False

        else:
            if not (byte & first_bit and not (byte & second_bit)):
                return False
        count_bytes -= 1
    return True
