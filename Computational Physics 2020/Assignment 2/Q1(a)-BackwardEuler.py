#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:34:54 2020

@author: ankit_090
"""

import numpy as np
import math 
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
#range
a=0
b=1

N=100 #no. of grid points 
h=(b-a)/N   #step size

x=np.arange(a,b,h)
y=np.zeros(N)
y[0]=y0=math.e

for i in range(1,N):
    def f(y):
        return (y-y0+h*9*y)
    y[i]=fsolve(f,y0)  # function used to solve non linear equation
    y0=y[i]    
plt.plot(x,y,'*',label='Backward Euler Solution')
plt.plot(x,np.exp(-9*x+1),label='Analytical solution')
plt.xlabel("x (arb. unit)")
plt.ylabel("y (x)")
plt.legend()
plt.savefig('Q1(a).pdf',dpi=1000)
plt.show()
    
