#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    arr=[]
    ns=[]
    for i in range(len(a)):
        if a[i] in a:
            c2=a.count(a[i])
            arr.append(c2)

        if a[i]+1 in a:
            c2=a.count(a[i])
            c3=a.count(a[i]+1)
            arr.append(c2+c3)
 
        if a[i]-1 in a:
            c1=a.count(a[i]-1)
            c2=a.count(a[i])
            arr.append(c1+c2)
            
            


    return(max(arr))

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
