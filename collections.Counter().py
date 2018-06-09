# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:52:48 2018

@author: NP
"""

X = int(input())
l = input().split(' ')
l = list(map(int, l))
c = int(input())
m = 0

for i in range(c):
    s = input().split(' ')
    s = list(map(int, s))
    if s[0] in l:
        m += s[1]
        l.remove(s[0])
        
print(m)        