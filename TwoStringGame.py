import math
import re


def twoStrings(s1, s2):
    s1_optimized = set(re.findall(r'[a-zA-Z]', s1))
    s2_optimized = set(re.findall(r'[a-zA-Z]', s2))

    if any(letter in s1_optimized for letter in s2_optimized):
        return "YES"
    return 'NO'
