# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:17:59 2018

@author: NP
"""

#!/bin/python3

import os
import sys

def getMoneySpent(keyboards, drives, b):
    sp = -1
    for i in keyboards:
        for j in drives:
            a = i + j
            if a > sp and a <= b:
                sp = a
    return sp
    
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
