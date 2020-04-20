#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 21:35:47 2020

@author: ankit_090
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

a=0
b=1
y0=0
N=20
h=(b-a)/N
x=np.arange(a,b+h,h)
def f(t,y):
    return t*np.exp(3*t)-2*y

sol= solve_ivp(f,[a,b],[y0],method='RK45',t_eval=x)
plt.plot(sol.t,sol.y[0,:],'*',label='numerical solution')
plt.plot(x,(np.exp(-2*x)*(1+np.exp(5*x)*(-1+5*x)))/25,label='analytical solution')

plt.xlabel("time (t)")
plt.ylabel("y (t)")
plt.legend()
plt.savefig('Q7(a).pdf',dpi=1000)
plt.show()

#print(sol.status)  # value 0 indicate that solution has converged