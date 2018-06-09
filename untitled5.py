# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:06:23 2018

@author: NP
"""

a = complex(input())
import math
print(math.sqrt(a.real**2 + a.imag**2))
print(math.atan2(a.imag,a.real))