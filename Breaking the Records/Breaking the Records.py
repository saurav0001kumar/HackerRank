#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mincount=0
    maxcount=0
    
    for i in range(len(scores)):
        if i==0:
            mini=scores[0]
            maxi=scores[0]
        else:
            if scores[i]>maxi:
                maxcount+=1
                maxi=scores[i]
            elif scores[i]<mini:
                mincount+=1
                mini=scores[i]

    return(maxcount,mincount)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
