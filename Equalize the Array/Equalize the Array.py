#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(a):
    dis=[]
    f=[]
    used=[]
    for i in range(len(a)):
        if a[i] not in used:
            c=a.count(a[i])
            f.append(c)
            used.append(a[i])
    m=max(f)
    return(len(a)-m)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
