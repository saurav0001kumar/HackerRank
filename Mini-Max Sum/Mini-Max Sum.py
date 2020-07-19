#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    z=(arr[0]+arr[1]+arr[2]+arr[3])
    arr=arr[::-1]
    print(z,arr[0]+arr[1]+arr[2]+arr[3])
    


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
