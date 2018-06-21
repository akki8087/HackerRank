# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 16:41:21 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    d = abs(x-z) - abs(y-z)
    if d == 0:
        return('Mouse C')
    elif d > 0:
        return('Cat B')
    elif d<0 :
        return('Cat A')
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
