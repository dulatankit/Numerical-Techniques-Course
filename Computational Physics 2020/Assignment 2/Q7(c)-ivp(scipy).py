#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:57:51 2020

@author: ankit_090
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
#range
a=1
b=2

y0=2
#no. of grid points
N=40
h=(b-a)/N  #stepsize

x=np.arange(a,b+h,h)
def f(t,y):
    return 1+y/t

sol= solve_ivp(f,[a,b],[y0],method='RK45',t_eval=x)

plt.plot(sol.t,sol.y[0,:],'*',label='numerical solution')
plt.plot(x,x*(2+np.log(x)),label='analytical solution')
plt.xlabel("time (t)")
plt.ylabel("y (x)")
plt.legend()
#plt.savefig('Q7(c).pdf',dpi=1000)
plt.show()

#print(sol.status)