# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 01:02:33 2018

@author: NP
"""

n = int(input())
l = []
for i in range(n):
    l.append(input())
print(len(set(l)))    