#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(a):
    lo=0
    a1= list(filter(lambda x: (x%2 != 0) , a))
    while len(a1)>1:
        i=a.index(a1[0])
        a[i]+=1
        lo+=1
        if i==0:
            a[i+1]+=1
            lo+=1
        elif i==len(a)-1:
            a[i-1]+=1
            lo+=1
        else:
            if a[i+1]%2!=0:
                a[i+1]+=1
                lo+=1
            elif a[i-1]%2!=0:
                a[i-1]+=1
                lo+=1
            else:
                a[i+1]+=1
                lo+=1
        a1= list(filter(lambda x: (x%2 != 0) , a))
    if len(a1)==1:
        return("NO")
    else:
        return(lo)

    



    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
