#!/bin/python3

import os
import sys
from math import factorial
#
# Complete the handshake function below.
#
def handshake(n):
    if n==1:
        return 0
    else:
        val=factorial(n)//(2*factorial(n-2))
        return val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()
