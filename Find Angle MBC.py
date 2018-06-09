# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 12:42:30 2018

@author: NP
"""

ab = int(input())
bc = int(input())
import math
c = math.atan2(ab,bc)
c = math.degrees(c)
b = 90 - c
print('{}°'.format(round(c)))