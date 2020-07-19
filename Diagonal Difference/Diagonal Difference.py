#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    d1=0
    for i in range(len(arr)):
        d1+=arr[i][i]
    i=0
    j=len(arr)-1
    while (i<len(arr) and j>=0) :
        d1=d1-arr[i][j]
        i+=1
        j-=1
    if d1<0:
        return abs(d1)
    else:
        return d1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
