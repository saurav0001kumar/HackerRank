#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c, m):
    cc=sorted(c)
    print(cc)
    dist=[]
    for i in range(m-1):
        for j in range(cc[i],cc[i+1]):
            t=(cc[i+1]-cc[i])//2
            dist.append(t)
    dist.append(min(cc)-0)
    dist.append(n-1-max(cc))
    return(max(dist))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c, m)

    fptr.write(str(result) + '\n')

    fptr.close()
