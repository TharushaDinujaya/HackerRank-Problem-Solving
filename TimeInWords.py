import math


def timeInWords(h, m):
    # Write your code here
    numbers = (
        "o' clock", 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'half'
    )
    time = ''
    if (m <= 30):
        hour = numbers[h]
    else:
        hour = numbers[h+1]

    if (m <= 30):
        minutes = numbers[m]
    else:
        minutes = numbers[60-m]
    if (m == 0):
        time = hour + ' ' + minutes
        return time
    elif (m <= 30):
        if (m == 15 or m == 30):
            time = minutes + ' past ' + hour
        elif (m == 1):
            time = minutes + ' minute past ' + hour
        else:
            time = minutes + ' minutes past ' + hour
        return time
    else:
        if (m == 45):
            time = minutes + ' to ' + hour
        elif (m == 59):
            time = minutes + ' minute to ' + hour
        else:
            time = minutes + ' minutes to ' + hour
        return time
