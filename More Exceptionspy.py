# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 18:44:24 2018

@author: NP
"""

#Write your code here
class Calculator:
    def power(self,n,p):    
        if n >= 0 and p >= 0:
            return(n**p)
        else:
            return('n and p should be non-negative')