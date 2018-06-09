# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:32:48 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    print(" ".join(map(str, arr[::-1])))
    
