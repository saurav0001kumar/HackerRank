#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(a):
    i1=[]
    j1=[]
    ch='X'
    for i in range(1,n-1):
        for j in range(1,n-1):
            a1=int(a[i-1][j])
            a2=int(a[i][j-1])
            a3=int(a[i+1][j])
            a4=int(a[i][j+1])
            a0=int(a[i][j])
            if (a1 < a0) and (a2 < a0) and (a3 < a0) and (a4 < a0):
                i1.append(i)
                j1.append(j)
    for k in range(len(i1)):
        t1=a[i1[k]][0:j1[k]]
        t2=a[i1[k]][j1[k]+1:len(a[i1[k]])]
        a[i1[k]]=t1+ch+t2

    return(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
