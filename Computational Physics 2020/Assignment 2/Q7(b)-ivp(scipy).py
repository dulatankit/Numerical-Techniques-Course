#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:39:53 2020

@author: ankit_090
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#range
a=2
b=3

y0=1 #initial condition
N=40 #no. of grid points
h=(b-a)/N  #stepsize
x=np.arange(a,b+h,h)

def f(t,y):
    return 1-(t-y)**2

z=np.linspace(2,2.975,30)
sol= solve_ivp(f,[a,b],[y0],method='RK45',t_eval=x)
plt.plot(sol.t,sol.y[0,:],marker='*',label='numerical solution')
plt.plot(z,(1-3*z+z*z)/(-3+z),label='analytical solution in range t=(2,2.975)')

plt.xlabel("time (t)")
plt.ylabel("y (t)")
plt.legend()
plt.savefig('Q7(b).pdf',dpi=1000)
plt.show()

print("Solution does not converge for the all specified range, it start diverging near t=3")