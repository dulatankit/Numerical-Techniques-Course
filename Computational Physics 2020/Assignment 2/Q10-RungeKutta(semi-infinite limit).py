#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 06:43:04 2020

@author: ankit_090
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

N=20
a=0#-1
b=np.pi/2#1
h=(b-a)/N
t0=3.5e6
z0=np.arctan(t0)

x=a
y=np.zeros(N+1)
y[0]=w=1
def f(t,y):
    return 1/((y*np.cos(t))**2+(np.sin(t))**2)

for i in range(1,N+1):
    K1=h*f(x,w)
    K2=h*f(x+h/2,w+K1/2)
    K3=h*f(x+h/2,w+K2/2)
    K4=h*f(x+h,w+K3)
    w=w+(K1+2*(K2+K3)+K4)/6
    y[i]=w
    x=a+i*h

x=np.arange(a,b+h,h)
f2=interpolate.InterpolatedUnivariateSpline(x,y, k=3)
#f2=interpolate.interp1d(x,y,kind='cubic',fill_value='extrapolate')
#plt.plot(x,y,'*')
#x1=np.arange(0,np.pi/2,0.1)

#plt.plot(x1,f2(x1))
print("The value of the function at 3.5e6=",f2(z0))
plt.show()


