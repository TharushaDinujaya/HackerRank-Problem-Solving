import math


def saveThePrisoner(n, m, s):
    # Write your code here
    status = n >= 1 and n <= 10**9 and m >= 1 and m <= 10**9 and s >= 1 and s <= n
    if (status):
        m = m - 1
        t = m+s
        t = t % n
        if (t == 0):
            t = n
        return t
    else:
        return
