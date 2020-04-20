#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 05:54:04 2020

@author: ankit_090
"""

import numpy as np
import matplotlib.pyplot as plt

#range
a=0
b=1

#number of grid points
N=25

m=3

h=(b-a)/N  #stepsize
x=a
y=np.zeros((N+1,m)) #stores value of solution at grid N+1 grid points for m different variables
u=np.zeros(m)   # local array to store values at intermediate steps of loops

#initial condition
u[0]=y[0][0]=3
u[1]=y[0][1]=-1
u[2]=y[0][2]=1

#Initialisation (some version show error if we don't initialise)
K1=np.zeros(m)
K2=np.zeros(m)
K3=np.zeros(m)
K4=np.zeros(m)

#set of equation
def f(x,u1,u2,u3,j):
    if(j==0):
        return (u1+2*u2-2*u3+np.exp(-x))
    elif(j==1):
        return (u2+u3-2*np.exp(-x))
    elif(j==2):
        return (u1+2*u2+np.exp(-x))


for i in range(1,N+1):
    for j in range(0,m):
        K1[j]=h*f(x,u[0],u[1],u[2],j)
    for j in range(0,m):
        K2[j]=h*f(x+h/2,u[0]+K1[0]/2,u[1]+K1[1]/2,u[2]+K1[2]/2,j)
    for j in range(0,m):
        K3[j]=h*f(x+h/2,u[0]+K2[0]/2,u[1]+K2[1]/2,u[2]+K2[2]/2,j)
    for j in range(0,m):
        K4[j]=h*f(x+h,u[0]+K3[0],u[1]+K3[1],u[2]+K3[2],j)
    for j in range(0,m):
        u[j]=u[j]+(K1[j]+2*(K2[j]+K3[j])+K4[j])/6
        y[i][j]=u[j]
    x=a+i*h
 
x=np.arange(a,b+h,h)

plt.plot(x,y[:,0],marker='o',markersize=3.5, linewidth=1,label='u1')
plt.plot(x,y[:,1],marker='+',markersize=3.5, linewidth=1,label='u2')
plt.plot(x,y[:,2],marker='*', linewidth=1,label='u3')
plt.title("Fouth-order Runge-Kutta ",loc='center',fontsize=12,fontweight=0,color='orange')
plt.xlabel("time (t)")
plt.ylabel("u (x)")
plt.legend()
#plt.savefig('Q11graph.pdf',dpi=1000)
plt.show()
