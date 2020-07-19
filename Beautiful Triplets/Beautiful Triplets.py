#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, a):
    t=0
    for i in range(n):
        if (a[i]+d in a) and (a[i]+d+d in a):
            t+=1
    return(t)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
