#!/bin/python3

import math
import os
import random
import re
import sys

def binary_recur(arr,n,left,right):
    if right>=left:
        mid=(left+right)//2
        if arr[mid]==n:
            return mid
        elif arr[mid]<n:
            return binary_recur(arr,n,mid+1,right)
        elif arr[mid]>n:
            return binary_recur(arr,n,left,mid-1)
    else:
        return -1
# Complete the pairs function below.
def pairs(k, arr):
    count=0
    arr.sort()
    arr2=arr.copy()
    for i in arr:
        val=binary_recur(arr,i+k,0,n-1)
        if val!=-1:
            count+=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
