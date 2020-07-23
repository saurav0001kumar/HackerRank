#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    w=0
    if len(s)>0:
        w=1
        for i in range(len(s)):
            if s[i]>='A' and s[i]<='Z':
                w+=1
    return(w)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
