#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    res=[]
    l=list(s)
    l=list(filter(lambda x: x!=" " ,l))
    s=''.join(l)
    le=len(s)
    row=math.sqrt(le)
    row=int(row)
    if row**2 == le:
        row=int(row)
        col=row
    else:
        col=row+1
        row=int(row)
    for i in range(col):
        t=""
        for j in range(i,le,col):
            t=t+s[j]
        res.append(t)
        res1=" ".join(res)
    return(res1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
