#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    g=0
    while s>=p and s>=m:
        if g==0:
            g+=1
            s=s-p
        if p-d>m and s>=p-d:
            g+=1
            p=p-d
            s=s-p
        elif p-d<=m and s>=m:
                g+=1
                p=m
                s=s-m
    return(g)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
