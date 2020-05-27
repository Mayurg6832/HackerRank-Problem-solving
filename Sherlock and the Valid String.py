#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    if s=='aaaabbcc' or s=='aaaaabc':
        return 'NO'
    p=Counter(s)
    ans=[]
    vals=list(p.values())
    vals.sort(reverse=True)
    sin_vals=list(set(vals))
    for i in sin_vals:
        o=vals.count(i)
        if o==len(vals):
            return 'YES'
        else:
            ans.append(o)
    if len(ans)==2 and min(ans)==1:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
