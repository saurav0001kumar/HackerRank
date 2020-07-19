#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(a):
    li=[]
    while len(a)>1:
        li.append(len(a))
        a.sort()
        mini=min(a)
        c=a.count(mini)
        a=a[c:len(a)]
        for i in range(len(a)):
            a[i]=a[i]-mini
    if len(a)!=0:
        li.append(len(a))
    return(li)

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
