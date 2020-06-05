# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:55:37 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pf
import statistics


N=1024

np.random.seed(555)
x=np.random.rand(N)

noise=x[:1020]
#Psdt=np.zeros(205)
N=len(noise)

k=5 # no. of segments in which we divide the sample
m=int(N/5)  # no. of points in each segment of sample
Psdt=np.zeros(204)
pm=pf.PdfPages("Q4.pdf")

freq1=2*np.pi*np.fft.fftfreq(N)
FFT1=np.fft.fft(noise,norm='ortho')
PSD1=FFT1*np.conj(FFT1)
plt.plot(noise,label='random numbers')
plt.xlabel('time (arb.unit)')
plt.ylabel('Random numbers')
plt.title('Sample Plot')
pm.savefig()
plt.show()

ind1=np.argsort(freq1)


plt.plot(freq1[ind1],PSD1.real[ind1]/N,marker='o',c='r',label='Delta Function')
plt.xlabel('k (arb.unit)')
plt.ylabel('Spectral power density')
#plt.xlim(-301,301)
plt.title('Power spectrum of Sample')
plt.legend()
pm.savefig()
plt.show()

data=np.array_split(noise,k)
for i in range(k):
    freq=2*np.pi*np.fft.fftfreq(len(data[i]))
    index=np.argsort(freq)
    FFT=np.fft.fft(data[i],norm='ortho')
    PSD=FFT*np.conj(FFT)/len(data[i])
    plt.plot(freq[index],PSD[index].real,marker='o',label='bin -'+str(i+1))
    Psdt=Psdt+PSD

plt.xlabel('k (arb.unit)')
plt.ylabel('Spectral power density')
plt.title("Power spectrum in 5 Bins")
plt.legend()
pm.savefig()
plt.show()
index=np.argsort(freq)

plt.plot(freq[index],(Psdt[index]/k).real,marker='o',c='g')
plt.title('Binned power spectrum')
plt.xlabel('freq (arb.unit)')
plt.ylabel('Spectral power density')
#plt.xlim(-0.5,0.5)
plt.tight_layout()
pm.savefig()
pm.close()
plt.show()
print("Note: Max & Min value of k depends on the resolution at which we sample in x domain, but since here given data is not sampled but given by random numbers, so resolution is by default dx=1.0, changing the value of dx would change max and min of k")
print("\n\nMinimum value of k vector is ",freq1.min())
print("Maximum value of k vector is ",freq1.max())

I=(freq1.max()-freq1.min())*np.sum(Psdt)/len(Psdt)
print("\n\nvariance of input random array from binned power spectrum",I.real)

print("variance of input random array using library function",statistics.variance(noise))