#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def binary(arr,l,r,ele):
    mid=(l+r)//2
    if l<=r:
        if arr[mid]==ele:
            return mid
        elif arr[mid]>ele:
            return binary(arr,mid+1,r,ele)
        elif arr[mid]<ele:
            return binary(arr,l,mid-1,ele)
    else:
        return l

def climbingLeaderboard(lst, alice):
    ans=[]
    rank=[1]
    for i in range(1,len(lst)):
        if lst[i]==lst[i-1]:
            rank.append(rank[i-1])
        else:
            rank.append(rank[i-1]+1)
    for i in alice:
        if i>lst[0]:
            ans.append(1)
        elif i<lst[-1]:
            ans.append(rank[-1]+1)
        else:
            ans.append(rank[binary(lst,0,len(lst),i)])
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
