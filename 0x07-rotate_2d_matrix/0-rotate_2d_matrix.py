#!/usr/bin/python3
""" 2D rotate Matrix Script"""


def rotate_2d_matrix(matrix):
    """ rotate n * n 2D Matrix 90 degree clockwise"""
    copy = [[n for n in arr] for arr in matrix]
    n = len(matrix)
    for i in range(n):
        for j in range(n - 1, -1, -1):
            matrix[i][n - 1 - j] = copy[j][i]
