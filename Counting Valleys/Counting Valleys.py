#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level=0
    v=0
    for i in range(len(s)):
        if s[i]=='D':
            if level==0:
                v+=1
            level-=1
        elif s[i]=='U':
            level+=1
    return(v)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
