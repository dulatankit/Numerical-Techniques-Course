# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:12:11 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt
import timeit

start=timeit.default_timer()
x=np.random.random(10000)
end=timeit.default_timer()
print("Time taken is %0.2e sec" % (end-start))
count,bins,ignored=plt.hist(x, bins=10, range=(0,1),density=True,label='obtained PDF')
plt.plot(bins,np.ones_like(bins),linewidth=3,color='red',label='Required PDF')
plt.xlabel('$x$.')
plt.ylabel('PDF')
plt.legend()
plt.title("Random numbers generated for uniform PDF by np.random.randn")
plt.savefig("Q2.pdf")
plt.show()