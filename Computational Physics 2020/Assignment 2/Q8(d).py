#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 05:49:00 2020

@author: ankit_090
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp


a=0
b=np.pi
N=10
h=(b-a)/N

x=np.arange(a,b+h,h)
y=np.ones((2,x.size))  # here 2 because we have set of 2 first order differential equation, and 2nd argument stores the value of u1 and u2 at grid points

def f(x,y):
    return np.vstack((y[1],0.5*(1-y[1]**2-y[0]*np.sin(x))))

# here y[1] is 2nd array (u2) of y and y[0] is 1st array(u1) 
def bc(ya,yb):
    return np.array([ya[0]-2,yb[0]-2])

"""
here (ya[0]-k) is boundary condition for y at one end is k& (yb[0]-m) is boundary 
condition of y at other end i.e. m, (if u another constraint condition ley say 
for derivative of y at first end then ya[1] defines it
"""

sol=solve_bvp(f,bc,x,y)

x_plot = np.linspace(a, b, 100)
y_plot = sol.sol(x_plot)[0]
plt.plot(x_plot, y_plot,'*',label='numerical solution')
plt.plot(x_plot,2+np.sin(x_plot), linewidth=2,label='analytical solution')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
#plt.savefig("Q8(d)graph.pdf",dpi=1000)
plt.show()