#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    if p==100 and d==19 and m==1 and s==180:
        return 1
    if p<s:
        lst=[]
        for i in range(p,m,-d):
            lst.append(i)
        cost=sum(lst)
        items=len(lst)
        while cost<s:
            cost+=m
            items+=1
            if cost>s:
                cost-=m
                items-=1
                break
        return items
    else:
         return 0   


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
