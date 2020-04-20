#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 23:00:38 2020

@author: ankit_090
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
#range
a=0
b=1
y0=1 #intial condition
N=40 # no. of grid points
h=(b-a)/N #stepsize
x=np.arange(a,b+h,h)
def f(t,y):
    return np.cos(2*t)+np.sin(3*t)

sol= solve_ivp(f,[a,b],[y0],method='RK45',t_eval=x)  #RK45/RK23/Radau/BDF

plt.plot(sol.t,sol.y[0,:],'*',label='numerical solution')
plt.plot(x,(8-2*np.cos(3*x)+3*np.sin(2*x))/6,label='analytical solution')
plt.xlabel("time (t)")
plt.ylabel("y (x)")
plt.legend()
plt.savefig('Q7(d).pdf',dpi=1000)
plt.show()

#print(sol.status)