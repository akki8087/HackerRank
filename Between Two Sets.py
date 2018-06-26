# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:06:25 2018

@author: NP
"""

#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    li = []
    for i in range(max(a),(min(b))+1):        
        c = 0
        for j in a:
            if i%j == 0:
                c += 1
        if c == len(a):
            l = 0
            for k in b:
                if k%i == 0:
                    l += 1
            if l == len(b):
                li.append(i)
                
    return len(li)
    
    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
