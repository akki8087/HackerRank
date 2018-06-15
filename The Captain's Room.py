# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:56:43 2018

@author: NP
"""

n = int(input())
ar = list(map(int,input().split()))
a = set(ar)
print(int((sum(ar)-(sum(a)*n))/-(n-1)))
