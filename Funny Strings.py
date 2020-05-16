#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    ans_s=[]
    ans_s_=[]
    s_=s[::-1]
    for i in range(len(s)-1):
        ans_s.append(abs(ord(s[i])-ord(s[i+1])))
        ans_s_.append(abs(ord(s_[i])-ord(s_[i+1])))
    
    if ans_s==ans_s_:
        return 'Funny'
    else:
        return 'Not Funny'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
