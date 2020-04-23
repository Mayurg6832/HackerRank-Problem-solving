#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    i=0
    a.sort()
    lst=[[a.pop(0)]]
    while a:
        if a[0] in lst[i]:
            lst[i].append(a.pop(0))
        else:
            if all(abs(a[0]-o)==1 for o in lst[i]):
                lst[i].append(a.pop(0))
            else:
                lst.append([a.pop(0)])
                i+=1
    mx=0
    for i in lst:
        if len(i)>mx:
            mx=len(i)
    return mx



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
