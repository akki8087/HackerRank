# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 00:42:59 2018

@author: NP
"""

n = int(input())
li = {}
o = []
for i in range(n):
    l = input().split()
    m = l.pop(-1)
    c = ' '.join(l) 
    if c not in o:
        o.append(c)
    if c in li:
        li[c] += int(m)       
    else:
        li[c] = int(m)
for j in o:    
    p = ' '.join([str(j),str(li[j])])
    print(p)
    