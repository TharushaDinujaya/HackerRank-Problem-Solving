import math


def catAndMouse(x, y, z):
    a = [x, y, z]
    if (max([x, y, z]) > 100 or min([x, y, z]) < 1):
        return
    elif (abs(z-x) > abs(z-y)):
        return "Cat B"
    elif (abs(z-x) < abs(z-y)):
        return "Cat A"
    elif (abs(z-x) == abs(z-y)):
        return "Mouse C"
    else:
        return
