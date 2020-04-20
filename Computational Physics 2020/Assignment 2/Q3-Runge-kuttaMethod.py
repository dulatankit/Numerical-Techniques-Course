#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 01:23:50 2020

@author: ankit
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:30:37 2020

@author: ankit
"""

import numpy as np
import matplotlib.pyplot as plt
#range
a=0
b=1

N=20  #no. of grid points
m=2 # order of equation

h=(b-a)/N   #stepsize
x=np.zeros(N+1)
x=a
y=np.zeros((N+1,m))   #stores value of solution at  N+1 grid points for m different variables
u=np.zeros(m)    # local array to store values at intermediate steps of loops

# initial condition
u[0]=y[0][0]=0
u[1]=y[0][1]=0

#Initialisation (some version show error if we don't initialise)
K1=np.zeros(m)
K2=np.zeros(m)
K3=np.zeros(m)
K4=np.zeros(m)

def f(x,u1,u2,j):
    if(j==0):
        return u2
    elif(j==1):
        return 2*u2-u1+x*(np.exp(x)-1)


for i in range(1,N+1):
    for j in range(0,m):
        K1[j]=h*f(x,u[0],u[1],j)
    for j in range(0,m):
        K2[j]=h*f(x+h/2,u[0]+K1[0]/2,u[1]+K1[1]/2,j)
    for j in range(0,m):
        K3[j]=h*f(x+h/2,u[0]+K2[0]/2,u[1]+K2[1]/2,j)
    for j in range(0,m):
        K4[j]=h*f(x+h,u[0]+K3[0],u[1]+K3[1],j)
    for j in range(0,m):
        u[j]=u[j]+(K1[j]+2*(K2[j]+K3[j])+K4[j])/6
        y[i][j]=u[j]
    x=a+i*h
 
x=np.arange(a,b+h,h)
plt.plot(x,y[:,0],'*',label='Numerical Solution')
plt.plot(x,-2-x+(np.exp(x)*(12-6*x+x**3))/6,label='Analytical solution')
plt.xlabel("x (arb. unit)")
plt.ylabel("y (x)")
plt.legend()
plt.savefig('Q3graph.pdf',dpi=1000)

plt.show()
    