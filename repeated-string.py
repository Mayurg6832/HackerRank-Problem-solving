#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
s=input()
n=int(input())
s_n=s.count("a")
nn=n//len(s)
ress=s_n*nn
if len(s) != 1:
    ree2=s[:n%len(s)].count("a")
    print(ress+ree2)
else:
    print(ress)
