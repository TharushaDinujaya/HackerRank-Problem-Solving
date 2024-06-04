import math


def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    i = 0
    while (i < len(c) - 1):
        if (i < len(c) - 2 and c[i+2] == 0):
            i += 2
            jumps += 1
        else:
            i += 1
            jumps += 1
    return jumps


print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))  # 4
