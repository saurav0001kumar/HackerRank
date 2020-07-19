#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    t=n
    ctr=0
    while n>0:
        dig=n%10
        n=n//10
        if dig==0:
            dig=0
        else:
            if t%dig==0:
                ctr+=1
    return(ctr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
