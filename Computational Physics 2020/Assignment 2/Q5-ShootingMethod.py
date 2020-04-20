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
b=10

N=100  #no. of grid points
m=2   #order of equation

h=(b-a)/N
x=np.zeros(N+1)
x=a
y=np.zeros((N+1,m))   #stores value of solution at grid N+1 grid points for m different variables
u=np.zeros(m)    # local array to store values at intermediate steps of loops

u[0]=y[0][0]=0  #boundary condition at one end
u[1]=e=46     # random guess to the initial condition for the y'
c=0  # boundary condition at other end

#z=np.zeros((N+1,3))   # array to store the 3 candidate solution, which is needed to plot
#w=np.zeros((N+1,3))   # array to store the 3 candidate solution, which is needed to plot
k=0  
ph=10 #local variable which carry the value of error at iteration within loop
AERR=0.0001  # max error at other boundary

#Initialisation (some version show error if we don't initialise)
K1=np.zeros(m)
K2=np.zeros(m)
K3=np.zeros(m)
K4=np.zeros(m)
phi=np.zeros(50)  # local array which stores the value of error at boundary point, 
                    #this has been used in sencant method.
                    # Here arguement is the maximum no. of iteration to find the true intial condition for y'
t=np.arange(a,b+h,h)
def f(x,u1,u2,j):
    if(j==0):
        return u2
    elif(j==1):
        return -10#2*u2-u1+x*(np.exp(x)-1)

while(abs(ph)>AERR):        # loop to find the correct initial condition for y' 
   
    for i in range(1,N+1):          #Runge-Kutta 4th order to find sol for any given initial condition for y'
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
    
    plt.plot(t,y[:,0],label=str("Iteration no. %.2f" % k))      # printing the value of y
    plt.axhline(0)
    plt.legend()
    
    #for i in range(1,N+1):     #this loop is used just to plot 5 candidate solution 
       # z[i][k]=y[i][0]
    
    phi[k]=y[N][0]-c   #error at boundary value
    ph=phi[k]
    k=k+1
    if k<2:
        u[0]=y[0][0]=0
        u[1]=r=54      # 2nd random guess of initial value of y' (since we are using secant method which require 2 initial guess)
        x=a
        
    else :
        u[0]=0
        u[1]=r-((r-e)*phi[k-1])/(phi[k-1]-phi[k-2])         #secant method to solve y(b,t)-c=0 i.e. to find correct t(initial value for y')
        e=r
        r=u[1]
        x=a
        
plt.show()
print("Total number of iteration taken to converge within Tolerance=1e-4 are =",k)

"""
plt.plot(t,w[:,0],marker='o',markersize=1.5) 
plt.plot(t,w[:,1],marker='o',markersize=2)
plt.plot(t,w[:,2],'o',markersize=2,label='numerically true solution')
plt.plot(t,z[:,0],marker='o',markersize=2)
plt.plot(t,z[:,1],marker='o',markersize=2)
plt.plot(t,-5*t*t+50*t,label='Analytical solution')
plt.title("Five candidate solution for shooting method")
plt.axhline(0)
plt.xlabel("time (t)")
plt.ylabel("x (t)")
plt.legend()
#plt.savefig('Q5graph.pdf',dpi=1000)
plt.show()
  
"""  