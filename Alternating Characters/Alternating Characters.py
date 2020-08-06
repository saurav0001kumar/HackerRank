#!/bin/python3
import collections as co
import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    s=list(s)
    fr=co.Counter(s)
    c=0
    if len(fr)==1:
        vals=fr.values()
        vals=list(vals)
        c=vals[0]-1
        return(c)
    else:
        t=s.copy()
        j=0
        for i in range(len(s)-1):
            if s[j]==s[j+1]:
                s.pop(j+1)
                c+=1
            elif s[j]!=s[j+1]:
                j+=1
        return(c)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
