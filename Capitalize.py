# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 14:51:10 2018

@author: NP
"""

def solve(s):
        
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return(s)  