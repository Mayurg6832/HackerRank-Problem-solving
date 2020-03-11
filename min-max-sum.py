#!/bin/python3
from itertools import combinations
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    maxsum=0
    minsum=float('inf')
    lst=combinations(arr,4)
    for i in lst:
        sum0=sum(i)
        if sum0<minsum:
            minsum=sum0
        if sum0>maxsum:
            maxsum=sum0
    print(minsum,maxsum)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
