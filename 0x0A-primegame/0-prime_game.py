#!/usr/bin/python3
''' prime game '''

"""
def is_prime(n):
    ''' checking if number is prime'''
    if n <= 1:
        return False
    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False

    # we used step 2 in range to eleminate the even divisors
    # because if n where divisible by any even number it would have been
    # divisible by 2 and thus already returned as not prime

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
"""


def sieve_of_eratosthenes(n):
    """Generate primes using Sieve of Eratosthenes up to n."""
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] is True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prime[0], prime[1] = False, False  # 0 and 1 are not primes
    return [p for p in range(n+1) if prime[p]]


def count_prime_number(x):
    ''' counting how many prime in the list'''
    return [len(sieve_of_eratosthenes(num)) for num in x]


def isWinner(x, nums):
    ''' function to check the winner'''
    ben = 0
    maria = 0
    primes = count_prime_number(nums[:x])
    for count in primes:
        if count % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return 'Ben'
    elif maria > ben:
        return 'Maria'
    else:
        return None
