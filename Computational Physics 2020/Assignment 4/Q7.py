# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:16:30 2020

@author: Ankit Dulat
"""

import numpy  as np
from scipy.stats import chi2

#Look up at lecture 22
def P(x):
    if (x<1 or x>99):
        print("Not Sufficiently random")
    if ((x>1 and x<5) or (x>95 and x<99)):
        print("Suspect")
    if ((x>5 and x<10) or (x>90 and x<95)):
        print("Almost Suspect")
    if (x>10 and x<90):
        print("Sufficiently random")

#Given data
s=np.array([2,3,4,5,6,7,8,9,10,11,12])
O1=np.array([4,10,10,13,20,18,18,11,13,14,13])
O2=np.array([3,7,11,15,19,24,21,17,13,9,5])
p=np.array([1,2,3,4,5,6,5,4,3,2,1])/36

n=144  #no. of times 2 dice was thrown (sum of all elements of O1)

V1=0
V2=0
for i in range(len(s)):    #calculating chi**2 for the 2 set of observation data
    V1=V1+(O1[i]-n*p[i])**2/(n*p[i])
    V2=V2+(O2[i]-n*p[i])**2/(n*p[i])

#now we determine "What si probability that V is this high"
    
k=float(11-1)   #Degree of freedom for the experiment, i.e. distinct values the random variable can have

P1=(1.0-chi2.cdf(V1,k))*100
P2=(1.0-chi2.cdf(V2,k))*100

print("Observation count1 are :")
P(P1)
print("\nObservation count2 are :")
P(P2)
        