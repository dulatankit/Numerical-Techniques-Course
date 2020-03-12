#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:06:39 2020

@author: ankit_090
"""

import numpy as np
import math 
import timeit

A=np.array([0,1,1,0,1,0,1,1,0,0,1,0,1,0,1]).reshape(5,3)

start=timeit.default_timer()

V=np.transpose(A)@A
S=A@np.transpose(A)


def eigen(A):
    eignval,eignvec=np.linalg.eigh(A)
    idx=eignval.argsort()[::-1]
    eignval=eignval[idx]
    eignvec=eignvec[:,idx]
    return (eignval,eignvec)


eignval1,eignvec1=eigen(S)
eignval2,eignvec2=eigen(V)
#eignval1,eignvec1=np.linalg.eigh(S)
#eignval2,eignvec2=np.linalg.eigh(V)

sigma=np.zeros((5,3))
T=np.zeros((5,5))

for i in range(0,5):
    for j in range(0,3):
        if i==j :
            sigma[i][j]=math.sqrt(eignval2[j])
        else:
            sigma[i][j]=0
for i in range(0,5):
    if i<3:
        T[:,i]=np.dot(A,eignvec2[:,i])/sigma[i][i]
    else:
        T[:,i]=eignvec1[:,i]
        
stop=timeit.default_timer()
print("Time taken by my code is:",stop-start,"sec\n\nSingular value calculated are:",sigma[0][0],sigma[1][1],sigma[2][2])


#print(sigma)
#print("\n\n\n\n\n",eignvec1)
start=timeit.default_timer()
a,b,c=np.linalg.svd(A)
stop=timeit.default_timer()
print("Time taken by library function is:",stop-start,"sec\n\nSingular value calculated by library are:",b)
#print(a)
#print(np.transpose(T))
#print("\n\n\n\n",(T@sigma)@np.transpose(eignvec2))
#print("\n\n\n\n",T)