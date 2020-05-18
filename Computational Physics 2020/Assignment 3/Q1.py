# -*- coding: utf-8 -*-
"""
Created on Sat May  9 19:28:20 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pf

N=256  #No. of smaple points
a=-100  #range of sampling
b=100
dx=(b-a)/N
x=np.arange(a,b,dx)
f=np.zeros(len(x))
g=np.zeros(N)

# defining function f(x)
for i in range(0,N):
    if x[i] == 0:
        f[i] = 1
    else:
        f[i]= np.sin(x[i])/x[i]



freq=2*np.pi*np.fft.fftfreq(N,d=dx)
#factor to be multiplied with DFT
alpha=dx*np.sqrt(N/(2*np.pi))*np.exp(-1j*freq*a)
FFT=alpha*np.fft.fft(f,norm='ortho')

pm=pf.PdfPages("Q1.pdf")

plt.figure()
plt.plot(x,f)
plt.title('Function f(x)')
plt.xlabel('x(arb. units)')
plt.ylabel('f(x)')

pm.savefig()
plt.show()


plt.plot(freq,FFT.real,label = 'Computed FT')
plt.xlim(-5, 5)

k=np.arange(freq.min(),freq.max()+freq[1],freq[1])
for i in range(0,N):
    if k[i] <1 and k[i] >-1:
        g[i] = np.sqrt(np.pi/2)

plt.plot(k,g,label= 'Analytical FT')
plt.title('Fourier transform F(k)')
plt.xlabel('k')
plt.ylabel('f(k)')
plt.legend()

pm.savefig()
pm.close()
plt.show()

