#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, a):
    li=[]
    for i in range(n):
        if i==0:
            li.append(a[i])
            c=ar.count(a[i])
            p=c//2
        elif a[i] not in li:
            li.append(a[i])
            c=ar.count(a[i])
            p+=c//2
    return(p)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
