# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 22:39:53 2018

@author: NP
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def staircase(n):
    for i in range(1,n+1):
        print(('#'*i).rjust(n,' '))
if __name__ == '__main__':
    n = int(input())

    staircase(n)
