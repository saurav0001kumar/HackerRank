#!/bin/python3
import collections as co
import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    b=list(b)
    count_=b.count("_")
    b=list(filter(lambda x: x!="_",b))
    s=co.Counter(b)
    k=list(s.keys())
    v=list(s.values())
    check=0
    for i in range(len(k)):
        t=b.index(k[i])
        for j in range(t,t+v[i]):
            if b[j]!=k[i]:
                check=1
                break
    if check==0 and 1 not in v:
        return("YES")
    elif check==0 and 1 in v:
        return("NO")
    elif check==1:
        if 1 in v:
            return("NO")
        elif 1 not in v and count_ >0:
            return("YES")
        else:
            return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
