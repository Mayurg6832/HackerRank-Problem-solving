#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k, n):
    e=100
    i=0
    if c[0]==1:
        e-=2
    while (i+k)%n != 0:
        if c[(i+k)%n]==1:
            e-=3
            i=((i+k)%n)
        else:
            e-=1
            i=((i+k)%n)
    return e-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k, n)

    fptr.write(str(result) + '\n')

    fptr.close()
