#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the equalizeArray function below.
def equalizeArray(arr):
    d=Counter(arr)
    d_values=list(d.values())
    d_key=list(d.keys())
    val=d_key[d_values.index(max(d_values))]
    return len(arr)-arr.count(val)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
