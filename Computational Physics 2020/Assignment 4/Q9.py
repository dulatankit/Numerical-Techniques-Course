# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:21:33 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.backends.backend_pdf as pf


n=10000     # No. of steps to genrate random no. 
theta=4.0    #1st random no. of the required PDF
L=[]        # To store the accepted random no. genrated
M=[]        # To store the rejected no.
mu=2
sigma=2

'''
def p(theta):
    return np.exp(-0.25*(theta-2)**2)*100
'''

def g(a):   #Sampling required for this unonormalised PDF
    if (a >= 3 and a < 7):
        return 5.0
    else:
        return 0.0

for i in range(n):
    #theta_prime = theta + np.random.standard_normal()
    theta_prime = np.random.uniform(-5,10)    # using uniform random no. genrator to genrate the candidates for random no. (above commented standard normal distribution function can also be used)
    r = np.random.rand()
    
    if (g(theta_prime)/g(theta)>r ):
        theta = theta_prime
    else:
        M.append(theta_prime)
    L.append(theta)
pm=pf.PdfPages("Q9.pdf")

plt.figure(figsize=(8,5))
x=np.arange(1,len(L)+1,1)  
plt.subplot(311)      
plt.plot(x,L,marker='o',markersize=2.5)
plt.xlim(1,100)
plt.ylabel("$\\theta$")
plt.title("Markov chains for 3 different number of steps")

plt.subplot(312)      
plt.plot(x,L,marker='o',markersize=2.5)
plt.xlim(1,500)
plt.ylabel("$\\theta$")

plt.subplot(313)      
plt.plot(x,L,marker='o',markersize=1.5)
plt.xlim(1,1000)


plt.xlabel("step")
plt.ylabel("$\\theta$")
plt.tight_layout()
pm.savefig()
plt.show()

x1=np.linspace(-5.0,10.0,len(L))
#plt.plot(x1,p(x1)/(100*np.sqrt(4*np.pi)))
count,bins,ignored=plt.hist(L,10,density=True)
plt.plot(bins,0.25*np.ones_like(bins),linewidth=3,color='red',label='Required')
plt.xlabel("$x$")
plt.ylabel("PDF")
plt.legend()
plt.title("PDF obtained using mcmc with 10000 points")
pm.savefig()
plt.show()
pm.close()
