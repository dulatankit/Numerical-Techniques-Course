# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:30:01 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):    #guassian distribution with mean 0 and variance 1
    return np.exp(-x*x/2)/(np.sqrt(2*np.pi))

x1=np.random.random(10000)
x2=np.random.random(10000)

y1=np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)
y2=np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)

x=np.arange(-5,5,0.1)
plt.plot(x,f(x),linewidth=3,label='Required PDF')
plt.hist(y1, bins=10,density=True,label='Obtained PDF')
plt.xlabel('$x$')
plt.ylabel('PDF')
plt.title('10,000 random number genrated by Box-Muller method')
plt.legend()
plt.savefig("Q5.pdf")
plt.show()