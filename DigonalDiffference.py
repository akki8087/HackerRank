# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 19:00:08 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(a):
    pd = 0
    ps = 0
    for i in range(len(a)):
        pd += a[i][i]  
        ps += a[len(a)-1-i][i]
    return(abs(pd - ps))    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    fptr.write(str(result) + '\n')

    fptr.close()
