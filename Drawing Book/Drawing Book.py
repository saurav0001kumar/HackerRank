#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    t1=0
    t2=0
    if p==1 or p==n:
        return(0)
    else:
        i=2
        while i<=p:
            if i%2==0:
                t1+=1

            i+=1
        
        i=n-1
        while i>=p:
            if i%2!=0:
                t2+=1

            i-=1
    if t1<t2:
        return(t1)
    else:
        return(t2)

    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
