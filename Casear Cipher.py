#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    ans=""
    for i in s:
        if i.isupper():
            ans+=chr((ord(i)+k-65)%26+65)
        elif i.islower():
            ans+=chr((ord(i)+k-97)%26+97)
        else:
            ans+=i
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
