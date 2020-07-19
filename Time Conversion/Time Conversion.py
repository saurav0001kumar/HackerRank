#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    t=s.split(":")
    if t[2][2] =='P' and t[0]=="12":
        t[2]=t[2][0:2]
        s=":"
        s=s.join(t)
        return(s)
    elif t[2][2] =='A' and t[0]=="12":
        t[2]=t[2][0:2]
        t[0]="00"
        s=":"
        s=s.join(t)
        return(s)    
    elif t[2][2] =='P':
        z=int(t[0])+12
        t[2]=t[2][0:2]
        t[0]=str(z)
        s=":"
        s=s.join(t)
        return(s)
    else:
        t[2]=t[2][0:2]
        s=":"
        s=s.join(t)
        return(s)

    #
    # Write your code here.
    #

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
