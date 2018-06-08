# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:56:17 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    total = 0
    for i in ar:
        total += i
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    
    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
