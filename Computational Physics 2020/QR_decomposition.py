#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 03:14:12 2020

@author: ankit
"""

import numpy as np
A=[[5,-2],[-2,8]]
eigval,eigvec=np.linalg.eigh(A)
print("Eigenvalues of the matrix using numpy is=",eigval)

k=1
TOL=1e-5
while abs(A[0][1])>TOL:
    Q,R=np.linalg.qr(A)
    A1=(np.transpose(Q)@A)@Q
    A=A1
    k+=1

print ('eigenvalues obtained form QR algorithm are :%.3f'%A[0][0],',%.3f'%A[1][1])
print ('number of QR-operations:',k)
    