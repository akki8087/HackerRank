# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 01:36:39 2018

@author: NP
"""

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    t = p // 2
    b = (n-p) // 2
    if n % 2 ==0 :
        b = ((n-p)+1)//2
        
    return min(t, b)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
