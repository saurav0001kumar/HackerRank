#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cloud=0
    jmp=0
    while cloud<=len(c)-3 :
        if cloud+2<=len(c)-1 and c[cloud+2]==0:
            cloud+=2
        else:
            cloud+=1
        jmp+=1
    if cloud==len(c)-2:
        jmp+=1
    return(jmp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
