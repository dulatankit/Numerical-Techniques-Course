# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:16:28 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt
import timeit

N=np.arange(4,101,4)
time1=np.zeros(len(N))
time2=np.zeros(len(N))
j=0

for i in N:
    t=np.arange(i)
    f=t*t
    
    #
    start1=timeit.default_timer()
      
    w=np.exp(-1j*2*np.pi/i)
    J,K = np.meshgrid(np.arange(i),np.arange(i))
    DFT = np.power(w,J*K)/np.sqrt(i)   #DFT matrix
    FFT1=DFT*f                 #FT from multiplication of DFT matrix with sampled function
    
    end1=timeit.default_timer()
    time1[j] = end1 - start1
    
    start2= timeit.default_timer()
    FFT2=np.fft.fft(f,norm='ortho')     #FT using FFT
    end2=timeit.default_timer()
    time2[j] = end2 - start2
    
    j = j+1

fig, ax1 = plt.subplots()
ax1.set_xlabel('No. of points used (n)')
ax1.set_ylabel('Time (sec) by Direct Computation')
ax1.plot(N,time1,marker='o',color='r')
ax1.tick_params(axis='y', labelcolor='r')
ax1.set_title('Time taken in computing FT')
ax2=ax1.twinx()
ax2.set_ylabel('Time (sec) by FFT', color='g')
ax2.semilogy(N,time2,marker='o',color='g')
fig.tight_layout()
plt.savefig("Q5.pdf",dpi=1000)
plt.show()

    
