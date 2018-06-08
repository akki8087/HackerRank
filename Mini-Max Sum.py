# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:58:59 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    s1 = sum(arr[0:4])
    s2 = sum(arr[1:5])
    s3 = sum(arr[2:5]) + arr[0]
    s4 = sum(arr[3:5]) + sum(arr[0:2])
    s5 = sum(arr[0:3]) + arr[4]
    li = [s1, s2, s3, s4, s5]
    maxi = max(li)
    mini = min(li)
    print('{} {}'.format(mini, maxi))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
