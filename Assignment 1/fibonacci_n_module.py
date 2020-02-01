# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:16:14 2019

@author: Ankit Dulat
"""

def fibonacci(n):
    a=0
    b=1
    L=[]
    for i in range (0,n):
        c=a+b
        #print(c)
        b=a
        a=c
        L.append(c)
    return(L)

