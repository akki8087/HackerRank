# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:33:14 2018

@author: NP
"""

n = int(input())
A = set(input().split())
m = int(input())
for i in range(m):
    o = input().split()[0]
    B = set(input().split())
    getattr(A, o)(B)
a = map(int, A)    
print(sum(a))    