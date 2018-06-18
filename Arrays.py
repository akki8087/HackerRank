# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 21:45:42 2018

@author: NP
"""
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

def arrays(arr):
    arr.reverse()
    return (numpy.array(arr,float))
    