#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    a1=math.sqrt(a)
    b1=math.sqrt(b)
    a1=int(a1)
    b1=int(b1)
    t=[int(i) for i in range(a1,b1+1)]
    t=list(filter(lambda x: (x*x>=a and x*x<=b),t))
    return(len(t))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
