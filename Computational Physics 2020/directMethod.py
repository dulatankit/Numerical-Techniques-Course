#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:50:36 2020

@author: ankit_090
"""

import numpy as np

A=np.array([1,0.67,0.33,0.45,1,0.55,0.67,0.33,1]).reshape(3,3)
B=np.array([2,2,2])
print("Solution is X:\n\n",np.linalg.solve(A,B))