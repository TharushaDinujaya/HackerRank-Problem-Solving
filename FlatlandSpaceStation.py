import math


def difference(a, b):
    return abs(a-b)


def flatlandSpaceStations(n, c):
    if (len(c) == n):
        return 0
    c.sort()
    start_distance = c[0] - 0
    end_distance = n - 1 - c[-1]
    distances = [start_distance, end_distance]

    if (len(c) > 1):
        max_distance = 0
        for i in range(1, len(c)):
            distance = difference(c[i], c[i-1])
            if (distance > max_distance):
                max_distance = distance
        max_distance = math.floor(max_distance/2)
        distances.append(max_distance)

    return max(distances)


print(flatlandSpaceStations(
    90, [4, 76, 16, 71, 56, 7, 77, 31, 2, 66, 12, 32, 57, 11, 19, 14, 42]))
