# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 09:29:06 2019

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

 #loading input data
frequency=np.loadtxt('data.txt',usecols=0)
cmb_flux=np.loadtxt('data.txt',usecols=1)

#constants
c=2.997e8
T=2.725
h=6.626e-34
k=1.38e-23

"""
Changing cm^(-1)  to Hz 
"""
frequency=(frequency*c*100)

#define function of spectral radiance for CMB

def specrad(x):
    return (2.*h*(x**3)/(c**2))*(1./(np.exp(h*x/(k*T))-1.))


plt.plot(frequency,cmb_flux*10**-20, marker='o',label='experimental data') # factor of 10^(-20) is multiplied to bring them at same scale
plt.plot(frequency,specrad(frequency), label='theortical curve')


plt.xlabel('frequency (Hz)')
plt.ylabel('Spectral radiance (W·sr-1·m−2·Hz−1)')
plt.title("Black-Body Spectrum")
plt.legend()
plt.savefig('spectrum.pdf',dpi=1000)
plt.show()
#plt.savefig('spectrum.pdf',dpi=1000)

BB = cmb_flux
peaks, _ = find_peaks(BB)
print('frequency(Hz) corrresponding to peak value is in the microwave region =',frequency[peaks])