import math


def diagonalDifference(arr):
    # Write your code here
    for x in arr:
        for y in x:
            if (y > 100 or y < -100):
                return
    d1, d2 = 0, 0
    length = len(arr[0])

    for x in range(0, length):
        d1 += arr[x][x]
        d2 += arr[x][length - 1 - x]

    if (d1 > d2):
        return d1-d2
    return d2-d1
