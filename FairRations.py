import math


def fairRations(B):
    # Write your code here
    count = 0
    B = list(map(int, B))
    for i in range(len(B)):
        if (B[i] % 2 == 1 and i < len(B) - 1):
            B[i] += 1
            B[i+1] += 1
            count += 2
        elif (B[i] % 2 == 1 and i == len(B) - 1):
            return "NO"
    return str(count)


print(fairRations([2, 3, 4, 5, 6]))  # 4
