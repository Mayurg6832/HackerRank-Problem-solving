#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    count=0
    lttr=list(map(chr, range(97, 123)))
    for i in lttr:
        if i not in s.lower():
            return 'not pangram'
    return 'pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
