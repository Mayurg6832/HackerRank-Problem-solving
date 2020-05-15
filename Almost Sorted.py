#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
	arr2=arr.copy()
	arr.sort()
	subs=[0]*len(arr)
	if arr2==arr:
		print('yes')
	else:
		for i in range(len(arr)):
			if abs(arr[i]-arr2[i])>0:
				subs[i]=1
		if subs.count(1)==2:
			ans=[j for j in range(len(subs)) if subs[j]==1]
			print("yes")
			print("swap",ans[0]+1,ans[1]+1)
		elif subs.count(1)>2:
			strt=subs.index(1)
			en=max(idx for idx, val in enumerate(subs)  
                                    if val == 1)
			print(strt)
			print(en)
			arr2=arr2[:strt]+arr2[strt:en][::-1]+arr2[en:]
			if arr2==arr:
				print("yes")
				print("reverse",strt+1,en)
			else:            
				print('no')
if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().rstrip().split()))
	almostSorted(arr)
