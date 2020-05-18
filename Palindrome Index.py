#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def is_palin(s,i,j):
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
def palindromeIndex(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            if is_palin(s,i+1,j):
                return i
            if is_palin(s,i,j-1):
                return j
        
            return -1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
