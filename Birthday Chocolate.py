# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 21:40:12 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s, d, m):
    c = 0
    for i in range(len(s)-m+1):
        su = 0
        for j in range(i,i+m):
            su += s[j]
        if su == d:
            c += 1
    return c        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = list(map(int, input().rstrip().split()))

    dm = input().split()

    d = int(dm[0])

    m = int(dm[1])

    result = solve(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
