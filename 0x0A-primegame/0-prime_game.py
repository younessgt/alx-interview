#!/usr/bin/python3
''' prime game '''


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False

    # we used step 2 in range to eleminate the even divisors
    # because if n where divisible by any even number it would have been
    # divisible by 2 and thus already returned as not prime

    for i in range(2, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def count_prime_number(x):
    return sum(is_prime(i) for i in range(1, x + 1))


def isWinner(x, nums):
    ben = 0
    maria = 0

    for num in nums:
        if count_prime_number(num) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return 'Ben'
    if ben < maria:
        return 'Maria'
    return None

