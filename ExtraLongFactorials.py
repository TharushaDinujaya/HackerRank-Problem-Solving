import math


def fact(n):
    if (n == 0):
        return 1
    return n*fact(n-1)


def extraLongFactorials(n):
    # Write your code here
    if (n > 100 or n < 0):
        return
    elif (n == 0):
        return 1
    else:
        print(fact(n))
