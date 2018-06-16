# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 21:13:25 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxn = scores[0]
    minn = scores[0]
    maxc = 0
    minc = 0
    for i in scores[1:]:
        if i > maxn:
            maxn = i
            maxc += 1
        elif i < minn:
            minn = i
            minc += 1
    return maxc,minc    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
