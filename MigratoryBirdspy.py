# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:37:14 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(ar):
    count = {}
    for i in range(1,6):
        count[i] = 0
        for j in ar:            
            if i == j:
                count[i] += 1
    key_max = max(count.keys(), key=(lambda k: count[k]))            
    return key_max
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = migratoryBirds(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
