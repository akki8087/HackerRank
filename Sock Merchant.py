# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 01:10:44 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    s = set(ar)
    match = 0
    for i in s:
        m = 0
        for j in ar:
            if i == j:
                m+=1
        match += m // 2        
    return match            
                
                
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
