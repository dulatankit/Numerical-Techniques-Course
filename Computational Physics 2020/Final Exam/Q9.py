# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:24:43 2020

@author: Ankit Dulat
"""
import numpy as np
import math 

p=input("enter 1 for finding singular values of matrix A \nenter 2 for finding singular values of matrix B\n")

if (int(p)==2):
    m=3
    n=3
    A=np.array([1,1,0,1,0,1,0,1,1]).reshape(m,n)
else:
    m,n=3,2
    A=np.array([2,1,1,0,0,1]).reshape(m,n)
    

V=np.transpose(A)@A
S=A@np.transpose(A)


def eigen(A):
    eignval,eignvec=np.linalg.eigh(A)
    idx=eignval.argsort()[::-1]  #reverse the order of argsort()
    
    eignval=eignval[idx]
    eignvec=eignvec[:,idx]
    return (eignval,eignvec)


eignval1,eignvec1=eigen(S)
eignval2,eignvec2=eigen(V)

sigma=np.zeros((m,n))
T=np.zeros((m,m))

for i in range(0,m):
    for j in range(0,n):
        if i==j :
            sigma[i][j]=math.sqrt(eignval2[j])
        else:
            sigma[i][j]=0

for i in range(0,m):
    if i<n:
        T[:,i]=np.dot(A,eignvec2[:,i])/sigma[i][i]
    else:
        T[:,i]=eignvec1[:,i]
if (int(p)==1):
    print("Two Singular value calculated Of matrix A are:\n",sigma[0][0],sigma[1][1])
else:
    print("Three Singular value calculated Of matrix B are:\n",sigma[0][0],sigma[1][1],sigma[2][2])

       

