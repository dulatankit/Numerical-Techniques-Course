#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 00:14:24 2020

@author: ankit
"""
import numpy as np
import matplotlib.pyplot as plt

#range
a=1
b=3

h=2#initial step size
TOL=0.0001 #Max absolute error at each step
k=0
#initialisation
x1=x2=a
w1=w2=-2 #initial condition

m=[]
n=[]
m.append(x1)
n.append(w1)

def f(t,y):
    #z=y/t
    return (y*y+y)/t#z*(1-z)

while(x1<b):
    
    K1=h*f(x1,w1)
    K2=h*f(x1+h/2,w1+K1/2)      #calculation with stepsize h
    K3=h*f(x1+h/2,w1+K2/2)
    K4=h*f(x1+h,w1+K3)
    y1=w1+(K1+2*(K2+K3)+K4)/6
    
    x2=x1
    w2=w1
    for j in range(1,3):
        K1=h*f(x2,w2)/2
        K2=h*f(x2+h/4,w2+K1/2)/2        #calculation with stepsize h/2 (2 iteration of h/2)
        K3=h*f(x2+h/4,w2+K2/2)/2
        K4=h*f(x2+h/2,w2+K3)/2
        y2=w2+(K1+2*(K2+K3)+K4)/6
        w2=y2
        x2=x2+j*h/2
        
    err=abs(y2-y1)
    if(err>TOL):
        q=(h*TOL/err)**(0.25)  # reduce the stepsize by this much factor(choosing some arbitrary factor can take many steps)
        h = q*h # Error is too large; decrease step size. NOTE: even when we use q=0.5 no. of iteration remains same
        print("step size changed =",h,"at ",k,"th iteration")
    
    elif (err < TOL/1000):
        h = 2*h # Larger error is acceptable; increase step size.
        print("step size changed to =",h,"at ",k,"th iteration")
    else:
        x1 = x1 + h
        w1=y1
        n.append(y1)
        m.append(x1)
    
    k=k+1
print("Total Number of iteration are",k)
x=np.array(m)
y=np.array(n)
s=-2.05*np.ones(len(x))  

fig,ax=plt.subplots()
ax.plot(x,y,'o',label='Adaptive Runge-kutta')
ax.plot(x,s,'o',markersize=3.5,label='meshpoint x')
ax.plot(x,2*x/(1-2*x),label='Analytical solution')
ax.set(title="with tol=0.00001",xlabel="time (t)", ylabel="y (x)")
plt.legend()  
plt.savefig("adaptive.pdf",dpi=1000)       
plt.show()
