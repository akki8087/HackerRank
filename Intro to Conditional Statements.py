# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:20:14 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if (N%2 != 0) or (N%2 == 0 and (N in range(6,21))):
        print('Weird')
    elif (N%2 == 0 and (N in range(2,6) or N > 20)):    
        print('Not Weird')