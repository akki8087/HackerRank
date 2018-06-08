# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:46:36 2018

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
    for i in range(1,11):
        print('{} x {} = {}'.format(n,i,n*i))