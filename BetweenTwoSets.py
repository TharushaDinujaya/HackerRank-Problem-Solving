import math
from functools import reduce


def multiply(a, b):
    return abs(a * b) // math.gcd(a, b)


def find_factors_count(n):
    count = 1
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            count += 1
    return count


def getTotalX(a, b):
    # Write your code here
    gcd = reduce(math.gcd, b)
    lcm = reduce(multiply, a)
    if gcd < lcm or gcd % lcm != 0:
        return 0
    elif gcd == lcm:
        return 1

    return find_factors_count(gcd / lcm)


a = [1]
b = [100]
print(getTotalX(a, b))  # 3
