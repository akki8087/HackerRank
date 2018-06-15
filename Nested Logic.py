# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 00:42:31 2018

@author: NP
"""

dr = list(map(int, input().split()))
dd = list(map(int, input().split()))

f = 0

if dr[2] > dd[2]:
    f = 10000
elif dr[2] == dd[2] and dr[1] > dd[1]:
    m = dr[1] - dd[1]
    f = 500 * m
elif dr[2] == dd[2] and dr[1] == dd[1] and dr[0] > dd[0]:
    d = dr[0] - dd[0]
    f = 15 * d

print(f)    