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

z=t/(1+np.log(t))
fig=plt.figure()
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
ax1.plot(t,y,marker='*',label='Euler solution')
ax1.plot(t,z,label='Analytical solution')
ax1.set(xlabel="time(t)",ylabel="y (t)")
plt.legend()

ax2.plot(t,abs(t-z)/t,marker='o',label='Relative Error')
ax2.plot(t,abs(t-z),marker='o',label='Absolute Error')
ax2.set(xlabel="time(t)",ylabel="Error")
plt.legend()
plt.savefig('Q2graph.pdf',dpi=1000)
plt.show()
    
