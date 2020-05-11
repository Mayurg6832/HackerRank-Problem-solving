#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    ans=[]
    for i in range(p,q+1):
        if i==1:
            ans.append(1)
        elif i>=9:
            num=i**2
            sp=len(str(num))//2
            if int(str(num)[:sp])+int(str(num)[sp:])==i:
                ans.append(i)
    if len(ans)>0:
        for i in ans:
            print(i,end=" ")
    else:
        print('INVALID RANGE')


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
