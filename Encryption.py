import math


def encryption(s):
    # Write your code here
    string_without_spaces = s.replace(" ", "")
    l = len(string_without_spaces)
    columns = math.ceil(l**0.5)
    rows = math.floor(l**0.5)
    encrypted_string = ""
    for i in range(columns):
        for j in range(0, l, columns):
            if (i + j >= l):
                break
            encrypted_string += string_without_spaces[i + j]
        encrypted_string += " "
    return encrypted_string


encryption("chillout")  # hae and via ecy
