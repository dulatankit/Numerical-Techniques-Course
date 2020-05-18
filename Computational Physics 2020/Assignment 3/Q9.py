# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:10:17 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt

N=256   #no. of smaple points
a=-3   #range of the sampling 
b=3
dx=(b-a)/N
x=np.arange(a,b,dx)
f=np.zeros(N)

for i in range(0,N):
    if x[i] <1 and x[i] >-1:        #define function
        f[i] = 1
kx=2*np.pi*np.fft.fftfreq(N,d=dx)
FFT=np.fft.fft(f,norm='ortho')
FFT=FFT**2     #product of fourier transform of functions
infft=dx*np.sqrt(N)*np.fft.ifft(FFT,norm='ortho')
plt.plot(x,np.fft.ifftshift(infft).real,marker='o',markersize='1',label='Convolution')
plt.plot(x,f,label='Box function')
plt.xlabel("x (arb.unit)")
plt.title("Convolution of the Box function")
plt.legend()
plt.savefig("Q9.pdf",dpi=1000)
plt.show()
