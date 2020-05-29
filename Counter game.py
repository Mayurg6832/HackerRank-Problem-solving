#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the counterGame function below.
def counterGame(n):
    turn=1
    while n!=1:
        if (n&(n-1))==0:
            n//=2
            turn= not turn
        else:
            p=n
            o=int(math.log(n,2))
            o=int(pow(2,o))
            n=p-o
            turn=not turn
    if turn==1:
        return 'Richard'
    else:
        return 'Louise'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
