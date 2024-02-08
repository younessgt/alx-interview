#!/usr/bin/python3
""" Script for solving N-queens problem """

from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
except Exception:
    print("N must be a number")
    exit(1)

coloumn = set()
diag_po = set()
diag_ne = set()

result = []
board = [[] * n for _ in range(n)]


def back_track(r, n, result, *arg):
    """solving N-queens problem using backtrack algo"""
    board, coloumn, diag_po, diag_ne = arg
    if r == n:
        new_board = [row for row in board]
        result.append(new_board)
        return

    for c in range(n):
        if c in coloumn or (r+c) in diag_po or (r-c) in diag_ne:
            continue
        coloumn.add(c)
        diag_po.add(r+c)
        diag_ne.add(r-c)
        board[r] = [r, c]

        back_track(r+1, n, result, board, coloumn, diag_po, diag_ne)
        coloumn.remove(c)
        diag_po.remove(r+c)
        diag_ne.remove(r-c)
        board[r] = []


back_track(0, n, result, board, coloumn, diag_po, diag_ne)
for res in result:
    print(res)
