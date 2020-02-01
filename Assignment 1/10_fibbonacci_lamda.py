# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:20:19 2019

@author: Ankit Dulat
"""

fibonacci = lambda n: n if n < 2 else fibonacci(n-1) + fibonacci(n-2)
print([fibonacci(i+1) for i in range(0,10)])
