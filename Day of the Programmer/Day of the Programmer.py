#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(y):
    
    if y>=1700 and y<=1917:
        if (y%4==0):
            d="12.09."+str(y)
        else:
            d="13.09."+str(y)
    elif y==1918:
        d="26.09."+str(y)
    else:
        if (y%100==0 and y%400==0) or (y%100!=0 and y%4==0):
            d="12.09."+str(y)
        else:
            d="13.09."+str(y)
    return(d)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
