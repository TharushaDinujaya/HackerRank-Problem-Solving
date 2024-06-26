import math


def isKap(x):
    if x == x**2:
        return True
    elif (len(str(x**2)) > 1):
        sq = str(x**2)

        left = sq[:len(sq)//2]
        right = sq[len(sq)//2:]

        if int(left) + int(right) == x:
            return True
        else:
            return False
    return False


def kaprekarNumbers(p, q):
    # Write your code here
    if (0 < p and p < q and q < 10**5):
        status = False
        for x in range(p, q+1):
            if (isKap(x)):
                print(x, end=' ')
                status = True
        if not (status):
            print("INVALID RANGE")
            return
    else:
        return
