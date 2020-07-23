#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, a):
    pg=0
    sp=0
    for i in range(n):
        tot=a[i]
        p=0
        while tot>0:
            if tot>=k:
                pg+=1
                tot=tot-k
                for j in range(p+1,p+k+1):
                    if j==pg:
                        sp+=1
                p+=k
            elif tot<k:
                pg+=1
                for j in range(p+1,p+tot+1):
                    if j==pg:
                        sp+=1
                p+=k
                tot=0
    return(sp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
