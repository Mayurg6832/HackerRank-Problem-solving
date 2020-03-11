#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    notes=Counter(note)
    magazines=Counter(magazine)

    for i in notes.keys():
        if i not in magazines.keys() or notes[i]>magazines[i]:
            print("No")
            return
    print("Yes")
    return
    

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
