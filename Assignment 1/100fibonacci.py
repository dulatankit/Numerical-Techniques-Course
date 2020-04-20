# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:55:40 2019

@author: Ankit Dulat
"""

import fibonacci_n_module as f 
print(f.fibonacci(100))

import timeit
mysetup="import fibonacci_n_module as f"
mycode="f.fibonacci(100)"
t=timeit.timeit(setup=mysetup,stmt=mycode,number=1000)
print("Time taken to print 100 fibonacci numbers:",t/1000)

#
