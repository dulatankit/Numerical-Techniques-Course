# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:08:55 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt

def f(a,b):     #given function
    if (a**2+b**2)<=1:
        return 1.0
    else:
        0.0

n=100000  #no. of random no. generated
k=0     #for count of random numbers falling within integrand function
r=1     # radius of circle

#intergration limit
a=-1
b=1
#To draw a circle, data generated
theta=np.linspace(0,2*np.pi,100)
x1=r*np.cos(theta)
y1=r*np.sin(theta)

x=np.random.uniform(a,b,n) #Random no. generated covering the integrand function
y=np.random.uniform(a,b,n)


plt.figure(figsize=(10,5))
plt.subplot(121)
plt.scatter(x,y,s=5,rasterized=True)
plt.plot(x1,y1,c= "red")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Random numbers alongwith circle")


x2=[]
y2=[]
for i in range(n):
    if f(x[i],y[i])==1:
        k +=1
        x2.append(x[i])
        y2.append(y[i])

plt.subplot(122)
plt.scatter(x2,y2,s=5,c="orange",label='Selected random points',rasterized=True)
plt.plot(x1,y1,c= "red")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend()
plt.savefig("Q8.pdf")
plt.show()  


area=((b-a)**2)*k/n
print("Area of circle is =",area)

radius=1.0
def nSphereVolume(dim, iteration):
    p = 0

    for i in range(iteration):
        r = np.random.uniform(-1.0, 1.0, dim)
        distance = np.linalg.norm(r)
        if distance < radius:
            p += 1

    return np.power(2.0, dim) * (p / iteration)

print("voluem of 10-d sphere of unit radii is =",nSphereVolume(10, 100000))