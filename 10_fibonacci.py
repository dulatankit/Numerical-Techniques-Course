# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:58:36 2019

@author: Ankit Dulat
"""
a=0
b=1
for i in range (0,10):
    c=a+b
    b=a
    a=c
    print(c)