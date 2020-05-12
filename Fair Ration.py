#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    count = 0
    for i in range(len(B)):
        if B[i]%2 == 1:
            B[i] += 1
            if i != len(B):
                try:
                    B[i+1] += 1
                except Exception:
                    return "NO"
            count+=2
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
