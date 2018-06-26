# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:53:03 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    import sys

    n = int(input().strip())
    tst = str(bin(n))
    tst = tst[2:]
    ones = 0
    maxOnes = 0
    for i in tst:
        if i == '1':
            ones += 1
            if maxOnes < ones:
                maxOnes = ones
        else:
            ones = 0 

    print(maxOnes)
    
    
    