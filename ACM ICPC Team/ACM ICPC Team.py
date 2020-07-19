#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(a):

    res=[]
    for i in range(len(a)-1):
        for k in range(i+1,len(a)):
            ctr=0
            for j in range(len(a[i])):
                if a[i][j]=='1' or a[k][j]=='1':
                    ctr+=1
            res.append(ctr)
        ctr=0
    maxi=max(res)
    c=res.count(maxi)
    return([maxi,c])
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
