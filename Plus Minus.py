# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:59:34 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        elif i == 0:
            zero += 1
    print(pos/n)
    print(neg/n)
    print(zero/n)
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
