# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:00:49 2018

@author: NP
"""

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(sum(map(lambda x: i * 10**x, range(i))))