#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    if len(s)%2!=0:
        return 'NO'
    opening=set('([{')
    sets=set([('(',')'),('[',']'),('{','}')])
    stack=[]
    for bracket in s:
        if bracket in opening:
            stack.append(bracket)
        else:
            if len(stack)==0:
                return 'NO'
            last_open=stack.pop()
            if (last_open,bracket) not in sets:
                return 'NO'
    if len(stack)==0:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
