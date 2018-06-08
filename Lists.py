# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:57:07 2018

@author: NP
"""

if __name__ == '__main__':
    N = int(input())
    def op(n):
        if n[0] == 'insert':
            l.insert(int(n[1]),int(n[2]))
        if n[0] == 'print':
            print(l)
        if n[0] == 'remove':
            l.remove(int(n[1]))
        if n[0] == 'append':
            l.append(int(n[1]))
        if n[0] == 'sort':
            l.sort()
        if n[0] == 'pop':
            l.pop()
        if n[0] == 'reverse':
            l.reverse()   
    l = []            
    for i in range(N):
        n = input().split()
        op(n)
        
        
        