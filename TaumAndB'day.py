import math


def taumBday(b, w, bc, wc, z):
    # Write your code here
    status = b >= 0 and w >= 0 and bc >= 0 and wc >= 0 and z >= 0
    status = status and b <= 10**9 and w <= 10**9 and bc <= 10**9 and wc <= 10**9 and z <= 10**9
    if (status):
        cost = 0
        if (max(bc, wc) - min(bc, wc) <= z):
            cost = b*bc + w*wc
        elif (bc > wc):
            cost = wc*(b+w) + b*z
        elif (wc > bc):
            cost = bc*(b+w) + w*z
        return cost
    else:
        return
