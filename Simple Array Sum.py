# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 19:00:50 2018

@author: NP
"""

#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #     
    total = 0    
    for i in ar:
        total += int(i)    
    return total  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
