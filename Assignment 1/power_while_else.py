# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:29:53 2019

@author: Ankit Dulat
"""

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

i = 0
while i < len(L):
 if 2**X == L[i]:
    print('2^5 found in list at index', i)
    break
 i=i+1
else:
    print(2**X, "not found")
  
