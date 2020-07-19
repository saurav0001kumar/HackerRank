#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus=0
    minus=0
    zero=0
    for i in range(len(arr)):
        if arr[i]>0 :
            plus+=1
        elif arr[i]<0 :
            minus+=1
        else:
            zero+=1
    print(plus/len(arr))
    print(minus/len(arr))
    print(zero/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
