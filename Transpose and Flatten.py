# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 00:20:33 2018

@author: NP
"""

import numpy
d = list(map(int,input().split()))
M = []
for i in range(d[0]):
    M.append(list(map(int,input().split())))
M = numpy.array(M)    

print(numpy.transpose(M))
print(M.flatten())
