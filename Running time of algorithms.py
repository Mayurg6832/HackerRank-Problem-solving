#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    count=0
    for i in range(1,len(arr)):
        ele=arr[i]
        j=i-1
        while j>=0 and arr[j]>ele:
            count+=1
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=ele
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
