#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    rev=s[::-1]
    l1=[]
    l2=[]
    for i in range(1,len(s)):
        t=abs(ord(s[i-1])-ord(s[i]))
        l1.append(t)
        t=abs(ord(rev[i-1])-ord(rev[i]))
        l2.append(t)
    if l1==l2:
        return("Funny")
    else:
        return("Not Funny")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
