#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(n, c,w,t):
    r=[]
    for i in range(t):
        m=0
        en=c[i][0]
        ex=c[i][1]
        for j in range(en,ex+1,1):
            if j==en:
                m=w[j]
            if w[j]<m:
                m=w[j]
        r.append(m)
    return(r)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases,width,t)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
