# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:21:37 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pf

N=128  #No. of smaple points
a=-10  #range of sampling
b=10
dx=(b-a)/N
x1=np.arange(a,b,dx)
x2=np.arange(a,b,dx/2)
x3=np.arange(a,b,dx/3)
f1=np.zeros(len(x1))
f2=np.zeros(len(x2))
f3=np.zeros(len(x3))
g=np.zeros(N)

# defining function f(x)
for i in range(0,N):
    if (x1[i]>-1 and x1[i] <1):
        f1[i] = 1
for i in range(0,2*N):
    if (x2[i]>-1 and x2[i] <1):
        f2[i] = 1
for i in range(0,3*N):
    if (x3[i]>-1 and x3[i] <1):
        f3[i] = 1


freq1=2*np.pi*np.fft.fftfreq(N,d=dx)
alpha1=dx*np.sqrt(N/(2*np.pi))*np.exp(-1j*freq1*a)
FFT1=alpha1*np.fft.fft(f1,norm='ortho')

freq2=2*np.pi*np.fft.fftfreq(2*N,d=dx/2)
alpha2=(dx/2)*np.sqrt(2*N/(2*np.pi))*np.exp(-1j*freq2*a)
FFT2=alpha2*np.fft.fft(f2,norm='ortho')

freq3=2*np.pi*np.fft.fftfreq(3*N,d=dx/3)
alpha3=(dx/3)*np.sqrt(3*N/(2*np.pi))*np.exp(-1j*freq3*a)
FFT3=alpha3*np.fft.fft(f3,norm='ortho')

pm=pf.PdfPages("Q10.pdf")

plt.figure()
plt.plot(x1,f1)
plt.title('Function f(x)')
plt.xlabel('x(arb. units)')
plt.ylabel('f(x)')
pm.savefig()
plt.show()

k=np.arange(freq1.min(),freq1.max()+freq1[1],freq1[1])

for i in range(0,N):
    if k[i] == 0:
        g[i] = np.sqrt(2/np.pi)
    else:
        g[i]= np.sqrt(2/np.pi)*np.sin(k[i])/k[i]
plt.plot(k,g,linewidth=3.0,label='Analytical')

idx1=np.argsort(freq1)
idx2=np.argsort(freq2)
idx3=np.argsort(freq3)

plt.plot(freq3[idx3],FFT3[idx3].real,marker='o',markersize=3.5,c='r',label = 'Computed FT1')

plt.title('Fourier transform F(k)')
plt.xlabel('k')
plt.ylabel('f(k)')
plt.legend()
pm.savefig()

plt.show()

plt.plot(freq1[idx1],FFT1[idx1].real,c='r',label = 'Computed FT1')
plt.plot(freq2[idx2],FFT2[idx2].real,label = 'Computed FT2')
plt.plot(freq3[idx3],FFT3[idx3].real,label = 'Computed FT3')
plt.title('Fourier transform F(k)')
plt.xlabel('k')
plt.ylabel('f(k)')
plt.legend()
pm.savefig()
pm.close()
plt.show()