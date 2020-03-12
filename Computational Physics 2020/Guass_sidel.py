#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 02:19:45 2020

@author: ankit
"""

import numpy as np
import math


A=np.array([0.2,0.1,1,1,0,0.1,4,-1,1,-1,1,-1,60,0,-2,1,1,0,8,4,0,-1,-2,4,700]).reshape(5,5)
B=np.array([1,2,3,4,5])
Xi=np.array([1.0,1.0,1.0,1.0,1.0])
x=np.zeros(5)
TOL=0.01
N=100
r=0
s=0

k=1
while k<N:
    for i in range(0,5):
        for j in range(0,i):
            r+=A[i][j]*x[j] 
        for j in range(i+1,5):
            s+=A[i][j]*Xi[j]
        x[i]=(-r-s+B[i])/A[i][i]
        r=0
        s=0
    max=math.sqrt(np.dot(x-Xi,x-Xi)/math.sqrt(np.dot(x,x)))
    if max<TOL:
        print("Solution is x=",x,"\nNumber of iteration =",k)
        break
    k+=1
    for i in range(0,5):
        Xi[i]=x[i]
else:
    print("Maximum number of iteration excedded")
    