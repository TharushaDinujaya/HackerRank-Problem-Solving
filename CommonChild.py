import math

def commonChild(s1, s2):
    for letter in s1:
        if letter not in s2:
            s1 = s1.replace(letter, "")
    
    for letter in s2:
        if letter not in s1:
            s2 = s2.replace(letter, "")

    if (len(s1) == 0):
        return 0
    elif(len(s1) <= len(s2)):
        n = len(s1)
    else:
        n = len(s2)

    s1 = s1
    s2 = s2
    count = [[0 for i in range(n)] for j in range(n)]

    for i in range(0, n):
        for j in range(0, n):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    count[i][j] = 1
                else:
                    count[i][j] = count[i-1][j-1] + 1
            else:
                count[i][j] = max(count[i-1][j], count[i][j-1])
    return count[n-1][n-1]


print(commonChild("AA","BB"))