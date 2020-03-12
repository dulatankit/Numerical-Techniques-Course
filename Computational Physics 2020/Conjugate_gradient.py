#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 02:36:21 2020

@author: ankit
"""

import numpy as np
import math


A=np.array([0.2,0.1,1,1,0,0.1,4,-1,1,-1,1,-1,60,0,-2,1,1,0,8,4,0,-1,-2,4,700]).reshape(5,5)
B=np.array([1,2,3,4,5])
C=np.identity(5)   # Precondition Matrix
x=np.array([1.0,1.0,1.0,1.0,1.0])
TOL=0.01
N=100

r=B-np.dot(A,x)
W=np.dot(C,r)
v=np.dot(np.transpose(C),W)
alpha=np.dot(W,W)

k=1
while k<N:
    if math.sqrt(np.dot(v,v))<TOL:
        print("Solution is x=",x,"\nNumber of iteration =",k)
        print("residual is r=",r)
        break
    
    
    u=np.dot(A,v)
    t=alpha/(np.dot(v,u))
    x+=t*v
    r-=t*u
    W=np.dot(C,r)
    beta=np.dot(W,W)
    
    if abs(beta)<TOL:
        if  math.sqrt(np.dot(r,r))<TOL:
            print("Solution is x=",x,"\nNumber of iteration =",k)
            print("residual is r=",r)
            break
    
    s=beta/alpha
    v=np.dot(np.transpose(C),W)+s*v
    alpha=beta
    k+=1
    
else:
     print("Maximum number of iteration excedded")
    



