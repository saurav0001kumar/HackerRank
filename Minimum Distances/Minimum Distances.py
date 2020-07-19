#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    used=[]
    mini=[]
    mindif=[]
    indices=[]
    for i in range(len(a)):
        if a.count(a[i]) >=2 and a[i] not in used:
            used.append(a[i])
            indices.clear()
            
            for j in range(len(a)):
                if a[i]==a[j]:
                    indices.append(j)
            indices.sort()
            
            for k in range(len(indices)):
                for m in range(len(indices)):
                    if k!=m:
                        mindif.append(abs(indices[k]-indices[m]))
            mini.append(min(mindif))
    
    if mini==[]:
        return(-1)
    else:
        return(min(mini))

    




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
