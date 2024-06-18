import math


def breakingRecords(scores):
    # Write your code here
    if (len(scores) >= 1 and len(scores) <= 1000 and min(scores) >= 0 and max(scores) <= 10**8):
        minCount = 0
        maxCount = 0
        minimum = scores[0]
        maximum = scores[0]
        for x in scores:
            if (minimum > x):
                minimum = x
                minCount += 1
            elif (maximum < x):
                maximum = x
                maxCount += 1
        return [maxCount, minCount]
    else:
        return
