# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:34:30 2019

@author: Ankit Dulat
"""

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

for i in L:
 if(i==2**X):
  print("2^5 found at index=",L.index(2**X))
  break
else:
  print(2**X, "not found")
  
