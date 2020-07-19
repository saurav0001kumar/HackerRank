#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    ctr=0
    
    for c in range(i,j+1):
        num=c
        rev=0
        while(num>0):
            dig=num%10
            rev=(rev*10)+dig
            num=num//10
        if abs(c-rev) % k == 0 :
            ctr+=1
    return(ctr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
