#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    i=0
    j=len(s)-1
    cnt=0
    while i<=j:
        if s[i]!=s[j]:
            mn=i if s[i]>s[j] else j
            cnt+=abs(ord(s[i])-ord(s[j]))
            i+=1
            j-=1
        else:
            i+=1
            j-=1
    return cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
