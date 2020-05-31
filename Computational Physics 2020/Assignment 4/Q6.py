# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:58:06 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pf 

def f(x):    #Required PDF 
    return np.sqrt(2/np.pi)*np.exp(-x*x/2)

def g(x):   #Envolpe function
    return 1.5*np.exp(-x)
N= 1000   #no. of random no. genrated for envolpe function, many of these will be rejected by required PDF
x=np.arange(0,10,0.1)

pm=pf.PdfPages("Q6.pdf")

plt.figure(figsize=(8,6))
plt.subplot(211)
plt.plot(x,f(x),label='Required PDF',linewidth=2)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(0,2)
plt.xlim(0,10)
plt.title("Random numbers genrated for Envolpe PDF")
plt.plot(x,g(x),label='Envolpe PDF')
plt.legend()

x1=np.random.rand(N)
x1=-np.log(2*x1)
y=np.random.rand(N)*g(x1)
plt.scatter(x1,y,marker='o',color='r',s=5)


yg = y[y<f(x1)]
xg = x1[y<f(x1)]

plt.subplot(212)
plt.plot(x,f(x),label='Required PDF',linewidth=2)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(0,2)
plt.xlim(0,10)
plt.title("Random numbers sampled in required PDF")

plt.plot(x,g(x),label='Envolpe PDF')
plt.legend()

plt.scatter(xg,yg,marker='o',color='r',s=5)
plt.tight_layout()
pm.savefig()
plt.show()

plt.plot(x,f(x),label='Required PDF',linewidth=2)
plt.hist(xg,range=(0.0,10.0),density=True,label='obtained PDF')
plt.ylim(0,1)
plt.xlim(0,10)
plt.ylabel("PDF")
plt.xlabel("$x$")
plt.legend()
plt.title("Density Histogram")
pm.savefig()
plt.show()
pm.close()