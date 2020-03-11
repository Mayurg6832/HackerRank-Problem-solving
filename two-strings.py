#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            print("YES")
            return
    print("NO")
    return


n=int(input())
for _ in range(n):
    s1=input()
    s2=input()
    twoStrings(s1,s2)
