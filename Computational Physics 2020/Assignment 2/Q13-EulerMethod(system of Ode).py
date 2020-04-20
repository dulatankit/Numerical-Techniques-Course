#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 06:19:07 2020

@author: ankit_090
"""

import numpy as np
import matplotlib.pyplot as plt

#range
a=1
b=2
N=30# no. of grid points
h=(b-a)/N
m=2 # order of equaiton / number of equation

t=a
y=np.zeros((N+1,m)) #stores value of solution at grid N+1 grid points for m different variables
u=np.zeros(m)  # local array to store values at intermediate steps of loops

#initial condition
u[0]=y[0][0]=1
u[1]=y[0][1]=0

def f(t,u1,u2,j):
    if(j==0):
        return u2
    elif(j==1):
        return ((2*u2/t)-(2*u1/(t*t))+t*np.log(t))

# Euler's Method
for i in range(1,N+1):
    for j in range(0,m):
        u[j]=u[j]+h*f(t,u[0],u[1],j)
        y[i][j]=u[j]
    x=a+i*h

t=np.linspace(a,b,N+1)
plt.plot(t,y[:,0],marker='o',markersize=3.5,label='Euler Method')
plt.plot(t,((7*t/4)+(0.5*t**3)*np.log(t)-(3/4)*t**3),marker='',label='Analytical Solution')
plt.title("Euler's Method ",loc='center',fontsize=12,fontweight=1,color='green')
plt.xlabel("time (t)")
plt.ylabel("y (x)")
plt.legend()
#plt.savefig('Q13graph.pdf',dpi=1000)
plt.show()
    