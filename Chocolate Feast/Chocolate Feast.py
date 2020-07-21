#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    wrap=0
    lw=0
    cho=0
    while n>=c or wrap>=m:
        if n>=c:
            t=n//c
            n=n-(t*c)
            cho+=t
            wrap+=t
        if wrap>=m:
            t=wrap//m
            wrap=wrap-(t*m)
            cho+=t
            wrap+=t
    return(cho)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
