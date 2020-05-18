# -*- coding: utf-8 -*-
"""
Created on Sun May 10 00:21:13 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt

N=1024   #NO. of sample points
a=-20    # range of smapling
b=20
dx=dy=(b-a)/N

x=np.arange(a,b,dx)
y=np.arange(a,b,dy)
xx,yy=np.meshgrid(x,y)

gauss= np.exp(-(xx**2+yy**2))     #2-d guassian fucntion sampled on 2-d grid
"""
plt.contourf(xx,yy,gauss)
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.colorbar()
plt.show()
"""

#plotting the sampled guassian funtion itself
plt.figure()
plt.pcolormesh(xx,yy, gauss, rasterized=True)
plt.title('Guassian function exp[-(x*x+y*y)]')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.xlabel('x (arb.unit)')
plt.ylabel('y (arb.unit)')
plt.gca().set_aspect("equal") 
plt.colorbar()
plt.show()

# calcultaing the frequency in fourier domain
kx= 2*np.pi*np.fft.fftfreq(N,d=dx)
ky= 2*np.pi*np.fft.fftfreq(N,d=dy)
kxx,kyy= np.meshgrid(kx,ky)

#these factors need to be multiplied to get continuous fourier transform from DFT
fac1=dx*np.sqrt(N/(2*np.pi))*np.exp(-1j*kxx*a)
fac2=dx*np.sqrt(N/(2*np.pi))*np.exp(-1j*kyy*a)

FFT=fac1*fac2*np.fft.fft2(gauss,norm='ortho')
kx1=np.fft.fftshift(kx)     #shifting the zero to the middle, actually this was required for these type of particular plots
ky1=np.fft.fftshift(ky)
kxx1,kyy1=np.meshgrid(kx1,ky1)

plt.figure()
plt.subplot(121)
plt.pcolormesh(kxx1,kyy1, np.fft.fftshift(FFT).real, rasterized=True)  #shifting the fourier values sicnce i shifted fourier frequency
plt.title('Fourier trnsform by FFT')
plt.xlabel('Kx')
plt.ylabel('Ky')
plt.xlim(-4,4)
plt.ylim(-4,4)
plt.gca().set_aspect("equal") 
plt.colorbar(fraction=0.046, pad=0.04)
#plt.show()


"""
plt.contourf(kxx,kyy,FFT.real)
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.colorbar()
plt.show()
"""

#plotting analytical fourier transform
g=0.5*np.exp(-0.25*(kxx1**2+kyy1**2))
plt.subplot(122)
plt.pcolormesh(kxx1,kyy1,g, rasterized=True)  # rasterized is used to reduce the image size saved, otherwise image size is 40mb.
plt.title('Analytical FFT')
plt.xlabel('Kx')
plt.ylabel('Ky')
plt.xlim(-4,4)
plt.ylim(-4,4)
plt.gca().set_aspect("equal") 
plt.colorbar(fraction=0.046, pad=0.04)
plt.tight_layout()
plt.savefig("Q8(a).pdf")
plt.show()

"""
plt.contourf(kxx,kyy,g)
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.colorbar()
plt.show()
"""



