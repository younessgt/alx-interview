#!/usr/bin/python3
""" script contain minOperations function"""


def minOperations(n):
    """ return the min number of operation (copy all, paste)
    nedeed to print n H charanters """

    sum = 0
    i = 2
    while (n > 1):
        if (n % i == 0):
            sum += i
            n = n / i
            i = 2
        else:
            i += 1
    return sum
