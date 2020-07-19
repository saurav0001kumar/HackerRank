#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    distinct1=[]
    f=[]
    d2=[]

    for i in range(len(arr)):
        if i==0:
            distinct1.append(arr[i])
            temp= arr.count(arr[i])
            f.append(temp)
        else:
            if arr[i] not in distinct1:
                distinct1.append(arr[i])
                temp= arr.count(arr[i])
                f.append(temp)
        
    t=max(f)
    
    
    for i in range(len(f)):
        if f[i]==t:
            d2.append(distinct1[i])
    
    d2.sort()
    
    return((d2[0]))

        

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
