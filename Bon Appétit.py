# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 21:49:17 2018

@author: NP
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = list(map(int,input().split()))
m = list(map(int,input().split()))
c = int(input())

items = n[0]
miss = n[1]

m.remove(m[miss])

ac = sum(m)/2
if c > ac:
    print(int(c-ac))
elif c == ac:
    print('Bon Appetit')