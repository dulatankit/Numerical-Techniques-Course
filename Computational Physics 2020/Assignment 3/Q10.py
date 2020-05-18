# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:57:07 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pf

noise=np.loadtxt(r'F:\Numerical-Techniques-Course-master\Computational Physics 2020\Assignment 3(Fourier Transform)\noise.txt')
Psdt=np.zeros(51)
N=len(noise)

k=10 # no. of segments in which we divide the sample
m=int(N/10)  # no. of points in each segment of sample

pm=pf.PdfPages("Q10.pdf")

freq1=2*np.pi*np.fft.fftfreq(N,d=0.01)
FFT1=np.fft.fft(noise,norm='ortho')
PSD1=FFT1*np.conj(FFT1)
plt.plot(noise)
plt.xlabel('time (arb.unit)')
plt.ylabel('Noise')
plt.title('noise signal')
pm.savefig()
plt.show()

ind1=np.argsort(freq1)
plt.plot(freq1[ind1],FFT1.real[ind1],marker='o',markersize='3.0')
plt.xlabel('freq (arb.unit)')
plt.ylabel('F(w)')
plt.title('DFT')
pm.savefig()
plt.show()

plt.figure(figsize=(12,4))
plt.subplot(121)
plt.plot(freq1[ind1],PSD1.real[ind1]/N,marker='o',markersize='3.0')
plt.xlabel('freq (arb.unit)')
plt.ylabel('Spectral power density')
#plt.xlim(-301,301)
plt.title('periodogram spectrum')
#plt.show()


data=np.array_split(noise,k)
for i in range(k):
    freq=2*np.pi*np.fft.fftfreq(len(data[i]),d=0.01)
    FFT=np.fft.fft(data[i],norm='ortho')
    PSD=FFT*np.conj(FFT)/len(data[i])
    #plt.plot(PSD.real)
    #plt.show()
    Psdt=Psdt+PSD
index=np.argsort(freq)

plt.subplot(122)
plt.plot(freq[index],(Psdt[index]/k).real,marker='o')
plt.title('Binned power spectrum')
plt.xlabel('freq (arb.unit)')
plt.ylabel('Spectral power density')
#plt.xlim(-301,301)
plt.tight_layout()
pm.savefig()
pm.close()
plt.show()

