#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    dic={}
    ans=[]
    for i in range(1,len(p)+1):
        dic[i]=p[i-1]
    key_list=list(dic.keys())
    value_list=list(dic.values())
    for i in range(1,len(p)+1):
        ans.append(key_list[value_list.index(key_list[value_list.index(i)])])
    
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
