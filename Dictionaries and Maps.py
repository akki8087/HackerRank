# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:46:04 2018

@author: NP
"""

n = int(input())
d = {}
for i in range(n):
    l = input().split()
    d[l[0]] = l[1]
while True:
    try:
        name = input() 
        if name in d:
            print('{}={}'.format(name,d[name]))
        else:
            print('Not found')
    except:
        break