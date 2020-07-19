#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    su=0
    for i in range(n):
        if i!=k:
            su+=bill[i]
            
    su=su//2
    if b==su:
        print("Bon Appetit")
    else:
        print(b-su)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
