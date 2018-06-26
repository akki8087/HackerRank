# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:39:31 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    ar = []
    h = []
    for _ in range(6):
        ar.append(list(map(int, input().rstrip().split())))
    for i in range(4):
        for j in range(4):
            a = ar[i][j]+ar[i][j+1]+ar[i][j+2]+ar[i+1][j+1]+ar[i+2][j]+ar[i+2][j+1]+ar[i+2][j+2]
            h.append(a)    
    #print(h)
    print(max(h))    