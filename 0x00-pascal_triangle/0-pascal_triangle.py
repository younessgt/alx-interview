#!/usr/bin/python3
""" Pascal's TRiangle script """


def pascal_triangle(n):
    """ function that return a list of lists of
    integers representing the Pascal’s triangle of n """

    if n <= 0:
        return []

    result = [[1]]

    for i in range(n - 1):
        temp_list = [0] + result[-1] + [0]
        row = []

        for j in range(len(result[-1]) + 1):
            row.append(temp_list[j] + temp_list[j + 1])
        result.append(row)

    return result
