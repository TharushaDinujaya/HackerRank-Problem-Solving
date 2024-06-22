import math


def timeConversion(s):
    # Write your code here
    if (len(s) == 10):
        status = s[0].isdecimal()
        status = status and s[1].isdecimal()
        status = status and s[2] == ':'
        status = status and s[3].isdecimal()
        status = status and s[4].isdecimal()
        status = status and s[5] == ':'
        status = status and s[6].isdecimal()
        status = status and s[7].isdecimal()
        status = status and (s[8] == 'P' or s[8] == 'A')
        status = status and s[9] == 'M'
        if (status):
            time = ''
            if (s[8] == 'A'):
                if (s[0]+s[1] == '12'):
                    time = '00'+s[2:8]
                else:
                    time = s[0:8]
            else:
                if (s[0]+s[1] == '12'):
                    time = s[0:8]
                else:
                    time = str(12 + int(s[0])*10 + int(s[1])) + s[2:8]
            return time
        else:
            return
