#!/bin/python3
from itertools import combinations
import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    lttrs=list(set(s))
    ans=[]
    combi=list(combinations(lttrs,2))
    for i in combi:
        lst=[]
        for j,k in enumerate(s):
            if k==i[0]:
                lst.append(0)
            elif k==i[1]:
                lst.append(1)
        flag=True
        for i in range(len(lst)-1):
            if lst[i] != abs(1-lst[i+1]):
                flag=False
        if flag:
            ans.append(len(lst))

    if (len(ans))>0:
        return max(ans)
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
