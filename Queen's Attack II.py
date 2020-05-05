#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    top  = n-r_q
    down = r_q-1
    left = c_q-1
    right= n-c_q
    upleftdig   =min(top,left)
    uprightdig  =min(top,right)
    downleftdig =min(down,left)
    downrightdig=min(down,right)
    
    for i in obstacles:
        r_o=i[0]
        c_o=i[1]

        if r_o==r_q and c_o<c_q:
            if c_q-c_o-1<left:
                left=c_q-c_o-1
        
        elif c_o==c_q and r_o > r_q:
            if r_o-r_q-1<top:
                top=r_o-r_q-1

        elif r_o==r_q and c_o>c_q:
            if c_o-c_q-1<right:
                right = c_o-c_q-1

        elif c_o==c_q and r_o < r_q:
            if r_q-r_o-1<down:
                down=r_q-r_o-1

        elif c_o>c_q and r_o>r_q:
            if c_o-c_q == r_o-r_q:
                if r_o-r_q-1<uprightdig:
                    uprightdig=r_o-r_q-1

        elif c_o>c_q and r_o<r_q:
            if c_o-c_q==r_q-r_o:
                if r_q-r_o-1<downrightdig:
                    downrightdig=r_q-r_o-1

        elif c_o<c_q and r_o>r_q:
            if c_q-c_o==r_o-r_q:
                if r_o-r_q-1<upleftdig:
                    upleftdig=r_o-r_q-1

        elif c_o<c_q and r_o<r_q:
            if c_q-c_o==r_q-r_o:
                if r_q-r_o-1<downleftdig:
                    downleftdig=r_q-r_o-1

    ans=top+down+left+right+uprightdig+upleftdig+downrightdig+downleftdig
    return ans



        
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
