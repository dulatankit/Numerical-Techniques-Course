#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 05:07:33 2020

@author: ankit
"""

import numpy as np
import matplotlib.pyplot as plt
import math 
#ramge
a=0
b=10
#boundary condition
y0=0
yN=0

N=20  # no. of grid points = no. of equation (since in this method each grid point form one equation)
k=0
p=10000 # maximum no. of iteration
TOL=0.001 # maximum error which you can afford

h=(b-a)/N
y=100*np.ones(N+1)   #it will store the final solution, here it is initialised by some guess value for the fixed point iteration (guass sidel) method
u=np.zeros(N+1)
n=1
x=a
y[0]=u[0]=y0  #end point are always fixed
y[N]=u[N]=yN   #end point are always fixed


#z=np.zeros((N+1,3))   # array to store the 10 candidate solution, which is needed to plot
t=np.arange(a,b+h,h)
def f(x,u0,u2):             # In general this is function of u0,u1,....,un variables but in this problem it comes out to be of just 2 variables
    return (u2+u0+h*h*10)/2

while (k<p):
    for i in range(1,N):
        if k<2:             #here this if else condition has been applied because we want to update our
            u0=y[i-1]       #initial guess for next iteration with the value which we have already calculated in the previous step for faster convergence.
        else:               
            u0=u[i-1]
        u2=y[i+1]
        u[i]=f(x,u0,u2)
        x=x+i*h
                                
    #Remove the comment if you want to see how the curve evolve to the exact curve
    if (k==3*n and k<16):
        plt.plot(t,u,label=str("Iteration no. %d" % k))
        plt.legend()
        n=n+1
    
    
        
    max=math.sqrt(np.dot(u-y,u-y)/math.sqrt(np.dot(u,u)))       #error calculation
    if max <TOL:
        
        plt.plot(t,u,'*',label=str("Final iteration %d" % k))
       
        plt.plot(t,-5*t*t+50*t,label='Analytical solution')
        plt.xlabel("time (t)")
        plt.ylabel("distance (x)")
        plt.legend()
        plt.title("Relaxation method with tolerance error = 0.001")
        #plt.savefig("Q6graph.pdf",dpi=1000)
        plt.show()
        
        break
    k+=1
    for i in range(0,N+1):
        y[i]=u[i]
    
    
else:
    print("maximum number of iteration excedded")

print("No. of iteration of fixed point iteration method to converge =",k)        


    
        