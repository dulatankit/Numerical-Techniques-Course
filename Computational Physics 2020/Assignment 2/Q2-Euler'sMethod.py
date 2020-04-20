#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:21:57 2020

@author: ankit
"""

import numpy as np
import matplotlib.pyplot as plt
#range
a=1
b=2

N=10    #no. of grid points
h=(b-a)/N   #step-size =0.1

t=np.arange(a,b+h,h)
y=np.zeros(N+1)
y[0]=y0=1   #initial condition

def f(y,t):
    z=y/t
    return z*(1-z)

for i in range(1,N+1):
    y[i]=y0+h*f(y0,t[i-1])
    y0=y[i]
    #print(y[i])    

plt.plot(t,y,marker='*',label='Euler solution')
plt.plot(t,t/(1+np.log(t)),label='Analytical solution')
plt.xlabel("time (t)")
plt.ylabel("y (t)")
plt.legend()
plt.savefig('Q2graph.pdf',dpi=1000)
plt.show()
    