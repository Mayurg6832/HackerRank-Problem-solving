  #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    sol=0
    i=1
    while True:
        if i**2>=a and i**2<=b:
            sol+=1
        if i**2>b:
            break
        i+=1
    return sol

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
