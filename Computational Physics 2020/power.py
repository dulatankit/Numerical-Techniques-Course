#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:35:16 2020

@author: ankit_090
"""

import numpy as np
A=np.array([2,-1,0,-1,2,-1,0,-1,2]).reshape(3,3)
N=10
v0=[1,1,1]
lemda0=15  #random guess
AERR=1e-5
i=0
while i<N:
    y=A@v0
    lemda=np.dot(y,v0)/np.dot(v0,v0)
    v0=y/abs(max(y, key=abs))
    if abs(lemda-lemda0)<AERR:
        print("maximum eigenvalues is ",lemda,"\n\nCorresponding Normalized eigenvector(by max. value) is",v0,"\n\nNumber of iteration taken is",i)
        break
    lemda0=lemda
    i+=1
else:
    print("Increase the number of iteration")
    


    
    
    
    