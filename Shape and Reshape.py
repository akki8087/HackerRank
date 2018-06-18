# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 23:05:00 2018

@author: NP
"""

import numpy
li = list(map(int, input().split()))
ar = []
for i in range(0,len(li)-2,3):
    ar.append([li[i],li[i+1],li[i+2]])
print(numpy.array(ar))

