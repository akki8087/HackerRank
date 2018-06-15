# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 01:57:15 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    t = n
    b = 0
    v = 0
    for i in s:
        if i == 'U':
            t += 1
        elif i == 'D':
            t -= 1
        if b+1 == n and t == n:
            v += 1
        b = t    
    return v    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
