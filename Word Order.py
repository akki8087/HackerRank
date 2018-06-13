# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 00:52:36 2018

@author: NP
"""

n = int(input())
d = {}
li = []
for i in range(n):
    c = input()
    if c not in li:
        li.append(c)
    if c in d:
        d[c] += 1
    else:
        d[c] = 1
print(len(d))        
for k in li:
    print(d[k], end=' ')
        
        