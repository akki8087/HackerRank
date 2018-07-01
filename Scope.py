# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 12:16:29 2018

@author: NP
"""

# End of Difference class
class Difference:
    def __init__(self, a):
        self.__elements = a
        maximumDifference = 0   
    def computeDifference(self):
        b = a[0]
        r = []
        for i in range(len(a)):
            for j in range(i,len(a)):
                r.append(abs(a[j]-a[i]))
        self.maximumDifference = max(r)    

a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)