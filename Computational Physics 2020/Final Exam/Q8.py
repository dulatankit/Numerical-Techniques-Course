# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 12:51:35 2020

@author: Ankit Dulat
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
import matplotlib.backends.backend_pdf as pf


a=0
b=1
N=10
h=(b-a)/N

x=np.arange(a,b+h,h)
y=np.zeros((2,x.size)) 

def f(x,y):
    return np.vstack((y[1],4*(y[0]-x)))

def bc(ya,yb):
    return np.array([ya[0],yb[0]-2])

def g(x):
    return (np.e)**2*(np.e**4-1)**(-1)*(np.exp(2*x)-np.exp(-2*x))+x

pm=pf.PdfPages("Q8.pdf")
sol=solve_bvp(f,bc,x,y)

x_p = np.linspace(a, b, 50)
y_p = sol.sol(x_p)[0]
plt.plot(x_p, y_p,'o',label="numerical solution")
plt.plot(x_p,g(x_p),linewidth=2,label='analytical solution')
plt.title("No. of iteration used, N =10")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
pm.savefig()
plt.show()

err=np.zeros(50)
print("x\tcalculated value\tanalytical value\terror(%)")
for i in range(1,50):
    err[i] = abs((g(x_p[i])-y_p[i])/g(x_p[i]))
    print(round(x_p[i],3),'\t',round(y_p[i],4),'\t',round(g(x_p[i]),4),'\t',err[i])
plt.semilogy(x_p,err,marker='o',label='Error')
plt.xlabel("x")
plt.ylabel("% error")
plt.legend()
pm.savefig()
pm.close()
plt.show()
