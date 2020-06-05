# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 17:41:09 2020

@author: Ankit Dulat

IN congruential method, depending on choice of parametrs the seed may repeat or may not be repeating, so value of parameters need to be chossen carefully.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pf



a=4452641
c=1013904223
m=4294967296
x=m/2
seed=x
n=10000
k=0

np.random.seed(545)
randm =np.zeros(n)

t=np.zeros(n)
r=np.zeros(n)
for i in range(n):
    r[i]=x
    x = (a*x+c)%(m)
    t[i]=i
    if(r[i]==seed):   #checking if seed repeats or not
        k=k+1

pm=pf.PdfPages("Q7.pdf")
     
plt.scatter(t,r,c='k',s=1.5)
plt.axhline(y=seed,linewidth=2.0,label='seed counts -'+ str(k))
plt.xlabel("$i$")
plt.ylabel("Random Numbers")
plt.title('Random distribution with non repetitive seed')
plt.legend()
pm.savefig()
plt.show()

a1=4452641
c1=1013904
m1=4295
x1=m1/2
seed1=x1
n1=1000
k1=0

np.random.seed(545)
randm =np.zeros(n1)

t1=np.zeros(n1)
r1=np.zeros(n1)
for i in range(n1):
    r1[i]=x1
    x1 = (a1*x1+c1)%(m1)
    t1[i]=i
    if(r1[i]==seed1):
        k1=k1+1
    
    
plt.scatter(t1,r1,c='k',s=1.5)
plt.axhline(y=seed1,linewidth=2.0,label='seed counts -'+ str(k1))
plt.xlabel("$i$")
plt.ylabel("Random Numbers")
plt.title('Random distribution with repetitive seed')
plt.legend()
pm.savefig()
pm.close()
plt.show()