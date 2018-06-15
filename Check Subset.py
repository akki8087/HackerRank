# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:07:39 2018

@author: NP
"""

T = int(input())
for _ in range(T):
    n = int(input())
    A = set(input().split())
    m = int(input())
    B = set(input().split())
    print(A.difference(B) == set())
