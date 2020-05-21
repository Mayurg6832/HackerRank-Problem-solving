#!/bin/python3
from collections import Counter

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    weights=set()
    ans=[]
    o=-1
    leng=0
    for i in s:
        weight=ord(i)-96
        weights.add(weight)
        if o==i:
            leng+=1
            weights.add(leng*weight)
        else:
            o=i
            leng=1
    for q in queries:
        if q in weights:
            ans.append('Yes')
        else:
            ans.append('No')
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
