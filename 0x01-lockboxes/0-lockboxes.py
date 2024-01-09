#!/usr/bin/python3
''' script to check if all boxes can be unlocked '''


def canUnlockAll(boxes):
    ''' function that return true if all boxes
    can be unlocked or false if not'''
    n = len(boxes)
    for i in range(0, n - 1):
        j = 0
        found = False
        for obj in boxes:
            if (i + 1) in obj and (i + 1) != j:
                found = True
                break
            j += 1
        if not found:
            return False
    return True
