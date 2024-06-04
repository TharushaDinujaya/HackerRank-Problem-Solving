import math


def biggerIsGreater(w):
    # Write your code here
    letters = list(w)

    if letters == sorted(letters, reverse=True):
        return "no answer"

    for i in range(len(letters)-2, -1, -1):
        temp_letters = letters[i+1:]
        temp_letters.sort()
        for j in range(len(temp_letters)):
            if temp_letters[j] > letters[i]:
                letters[i], temp_letters[j] = temp_letters[j], letters[i]
                temp_letters.sort()
                letters = letters[:i+1] + temp_letters
                return "".join(letters)


print(biggerIsGreater("lmno"))
