#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the acmTeam function below.
def acmTeam(topic):
    rtrn=[]
    ans=[]
    lst=list(range(1,len(topic)+1))
    lst=list(combinations(lst,2))
    for i in lst:
        m=0
        val=int(topic[i[0]-1])+int(topic[i[1]-1])
        n=str(val).count('0')
        m=len(str(val))-n
        ans.append(m)
    mx=max(ans)
    rtrn.append(mx)
    rtrn.append(ans.count(mx))
    return rtrn


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
