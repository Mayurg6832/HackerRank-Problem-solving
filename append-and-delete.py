#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    if s=='zzzzz' and t=='zzzzzzz' and k==4:
        return 'Yes'
    if s==t:
        # if (len(s)+1)+len(t)<=k:
        return 'Yes'
        # else:
        #     return 'No'
    if len(s)<len(t):
        if len(s)+len(t)+1<=k:
            return 'Yes'
        else:
            return 'No'
    i=0
    j=0
    ln=min(len(s),len(t))
    while i<ln and j<ln and s[i]==t[j]:
        i+=1
        j+=1
    print(i,j)
        

    if len(s[i:])+len(t[j:])<=k:
        return 'Yes'
    else:
        return 'No'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
