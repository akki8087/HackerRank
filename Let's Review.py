# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:20:47 2018

@author: NP
"""

n = int(input())
for c in range(n):
    even = ''
    odd = ''
    w = input()
    for i in range(len(w)):
        if i%2 == 0:
            even += w[i]
        elif i%2 != 0:
            odd += w[i]
    print(even+' '+odd)        