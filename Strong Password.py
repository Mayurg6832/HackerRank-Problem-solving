#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    conditions=4
    nums=False
    lowe=False
    uppr=False
    spe=False
    for i in password:
        if conditions > 0:
            if i in numbers and not nums:
                conditions-=1
                nums=True
            elif i in lower_case and not lowe:
                conditions-=1
                lowe=True
            elif i in upper_case and not uppr:
                conditions-=1
                uppr=True
            elif i in special_characters and not spe:
                conditions-=1
                spe=True
        else:
            break
    return max(conditions,6-n)

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
