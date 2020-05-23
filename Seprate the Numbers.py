#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    if len(s)==1:
        return 'NO'
    for i in range(1,len(s)//2+1):
        lst=[]
        lst.append(s[:i])
        while len(''.join(lst))<len(s):
            lst.append(str(int(lst[-1])+1))
        if ''.join(lst)==s:
            return 'YES '+lst[0]
        
    return 'NO'

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        print(separateNumbers(s))
