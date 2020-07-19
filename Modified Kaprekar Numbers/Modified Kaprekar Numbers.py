#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    kn=[]
    
    for i in range(p,q+1):
        if i==1:
            kn.append(1)
        elif i==9:
            kn.append(9)
        elif i>1 and i<9:
            kkk=0
        else:
            leng=len(str(i))
            sq=i**2
            s=str(sq)
            ln=len(s)
            l=s[0:ln-leng]
            l=int(l)
            r=s[ln-leng:ln]
            r=int(r)
            if l+r==i:
                kn.append(i)
    if len(kn)==0:
        print("INVALID RANGE")
    else:
        for i in range(len(kn)):
            print(kn[i],end=" ")


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
