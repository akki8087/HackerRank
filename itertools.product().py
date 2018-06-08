# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 19:04:08 2018

@author: NP
"""

A = input().split(' ')
B = input().split(' ')

for a in A:
    for b in B:
        t = (int(a), int(b))
        print(t, end = ' ')