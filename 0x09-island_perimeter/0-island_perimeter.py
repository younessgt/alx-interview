#!/usr/bin/python3
''' script to solve the island perimeter problem'''


def island_perimeter(grid):
    '''returning the perimeter of the island described in grid'''

    per = 0
    con = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            if grid[i][j] == 1:
                per += 4
                if grid[i - 1][j] == 1 and i != 0:
                    con += 1
                if grid[i][j - 1] == 1 and j != 0:
                    con += 1
    return per - (con * 2)
