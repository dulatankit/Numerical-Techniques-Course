# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:00:29 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt

N=512
a=-100
b=100
dx=(b-a)/N
x=np.arange(a,b,dx)
f=5*np.ones(len(x))

freq=2*np.pi*np.fft.fftfreq(N,d=dx)
#factor to be multiplied with DFT
alpha=dx*np.sqrt(N/(2*np.pi))*np.exp(-1j*freq*a)
FFT=alpha*np.fft.fft(f,norm='ortho')

plt.subplot(211)
plt.plot(x,f)
plt.title('Function f(x)=5')
plt.xlabel('x(arb. units)')
plt.ylabel('f(x)')

plt.subplot(212)
plt.plot(freq,FFT.real,marker='o',label = 'Computed FT',color='g')
plt.legend()
#plt.xlim(-0.5, 0.5)
plt.ylim(0, 450)
plt.title('Fourier transform F(k)=delta fuction')
plt.xlabel('k')
plt.ylabel('f(k)')
plt.tight_layout()
plt.savefig("Q6.pdf",dpi=1000)
plt.show()