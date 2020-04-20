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

N=50 #no. of grid points
h=(b-a)/N  #stepsize

x=np.arange(a,b,h)
y=np.zeros(N)
y[0]=y0=1/3 # intial condition

for i in range(1,N):
    def f(y):
        return (y-y0+h*(20*(y-x[i])**2-2*x[i]))
    y[i]=fsolve(f,y0)
    y0=y[i]
    #print(y[i])    

plt.plot(x,y,marker='*',markersize=3.5,label='Numerically calculated')
plt.xlabel("x (arb. unit)")
plt.ylabel("y (x)")
plt.legend()
plt.savefig('Q1(b).pdf',dpi=1000)
plt.show()
    
