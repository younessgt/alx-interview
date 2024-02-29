#!/usr/bin/python3
''' script to solve the coin change problem '''


def makeChange(coins, total):
    '''documentation needed'''
    if total == 0:
        return 0

    acc = [total + 1] * (total + 1)
    acc[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                j = i - coin
                acc[i] = min(acc[j] + 1, acc[i])
    if acc[total] == total + 1:
        return -1
    else:
        return acc[total]
