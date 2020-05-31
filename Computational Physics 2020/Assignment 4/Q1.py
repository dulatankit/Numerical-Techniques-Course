# -*- coding: utf-8 -*-
"""
Created on Wed May 27 10:27:41 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt
import timeit


a=1543794
c=1013759642
m=4632781205
x=1

n=10000
randm =np.zeros(n)
start=timeit.default_timer()

for i in range(n):
    x = (a*x+c)%m
    randm[i] = x
randm = randm/(np.amax(randm))   #dividing by maximum to obtain random in range (0,1)

end=timeit.default_timer()
print("Time taken is %0.2e sec" % (end-start))

count,bins,ignored=plt.hist(randm, bins=10,density=True,label='obtained PDF')
plt.plot(bins,np.ones_like(bins),linewidth=3,color='red',label='Required PDF')
plt.xlabel('$x$.')
plt.ylabel('PDF')
plt.legend()
plt.title("Random numbers generated for uniform PDF by congruential method")
plt.savefig("Q1.pdf")
plt.show()