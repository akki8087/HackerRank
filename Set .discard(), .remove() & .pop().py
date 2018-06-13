# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 01:18:37 2018

@author: NP
"""

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    k = input()
    if k == 'pop':
        s.pop()
    else:
        d = k.split()
        if d[0] == 'discard':
            s.discard(int(d[-1]))
        elif d[0] == 'remove':
            s.remove(int(d[-1]))
print(sum(s))            