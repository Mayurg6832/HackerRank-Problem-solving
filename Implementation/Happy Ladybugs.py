#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    di={}
    for i in b:
        if i!='_':
            if i not in di:
                di[i]=1
            else:
                di[i]+=1
    vals=list(di.values())
    if n==1 and b.count('_')==0:
        return 'NO'
    elif b.count('_')==1 and vals.count(1)==0:
        return 'YES'
    elif b.count('_')>1 and 1 not in vals:
        return 'YES'
    elif b.count('_')==0:
        for i in range(n):
            if i==0:
                if b[i]!=b[i+1]:
                    return 'NO'
            elif i==n-1:
                if b[i]!=b[i-1]:
                    return 'NO'
            else:
                if b[i]!=b[i-1] and b[i]!=b[i+1]:
                    return 'NO'
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
