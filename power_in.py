# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:43:18 2019

@author: Ankit Dulat
"""

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
if 2**X in L:
    print('2**5 found in list at index=',L.index(2**X))
    
else:
    print(2**X,'not found in the list')