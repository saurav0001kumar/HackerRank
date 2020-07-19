#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e=100
    i=0
    while(e!=0):
        if i+k < n:
            if c[i+k]==1:
                e=e-3
            else:
                e=e-1
        elif i+k>=n :
            t=len(c)-i
            z=k-t
            if c[z]==1 and z==0:
                e=e-3
                break
            elif c[z]==0 and z==0:
                e=e-1
                break
            elif c[z]==0 :
                e=e-1
                i=z-k
            elif c[z]==1 :
                e=e-3
                i=z-k
        i+=k
    return(e)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
