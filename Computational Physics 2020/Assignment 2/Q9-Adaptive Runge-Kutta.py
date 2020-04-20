# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 00:36:59 2020

@author: Ankit Dulat
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

#import plottools
def fun(t,x):
    # This is the right-hand side of the first-order ordinary differential 
    # equation dx/dt = fun.
    return (x*x+x)/t
    
# Set initial conditions.
a=1
b=3
y0=-2

t=a
x=y0

k=0
m=[]
n=[]
m.append(t)
n.append(x)

# Set initial step size.
dt = 1e-1
# Set relative change tolerances.
dx_max = 0.0001  # (absolute Tolerance)Enables faster speed.
dx_min = dx_max/2 # Controls accuracy.

while (t < b):

    
    # Calculate partial steps for stepsize dt.
    k1 = fun(t,      x)
    k2 = fun(t+dt/2, x+dt*k1/2)
    k3 = fun(t+dt/2, x+dt*k2/2)
    k4 = fun(t+dt,   x+dt*k3)
    step_x = x + dt/6*(k1+2*k2+2*k3+k4)

    # Calculate partial steps for stepsize dt/2.
    k2 = fun(t+dt/4, x+dt*k1/4)
    k3 = fun(t+dt/4, x+dt*k2/4)
    k4 = fun(t+dt/2, x+dt*k3/2)
    half_step_x = x + dt/12*(k1+2*k2+2*k3+k4)

    # Calculate partial steps for stepsize 2*dt.
    k2 = fun(t+dt,   x+dt*k1)
    k3 = fun(t+dt,   x+dt*k2)
    k4 = fun(t+2*dt, x+2*dt*k3)
    dble_step_x = x + dt/3*(k1+2*k2+2*k3+k4)

    if (abs(step_x-half_step_x) > dx_max):
        delta=abs(step_x-half_step_x)
        q=(dt*dx_min/delta)**(0.25)  # reduce the stepsize by this much factor(choosing some arbitrary factor can take many steps)
        dt = q*dt # Error is too large; decrease step size.
        print("step size changed to=",dt,"at ",k,"th iteration")
    elif (abs(step_x-dble_step_x)/abs(step_x) < dx_min):
        dt = dt*2 # Larger error is acceptable; increase step size.
        print("step size changed to =",dt,"at ",k,"th iteration")
    else:
        x = step_x
        t = t + dt
        n.append(x)
        m.append(t)
        
    k=k+1
 
print("Total Number of iteration are",k)
t=np.array(m)
x=np.array(n)
s=-2.05*np.ones(len(t))  

fig,ax=plt.subplots()
ax.plot(t,x,marker='o',markersize=1.5,label='Adaptive Runge-kutta')
ax.plot(t,s,'o',markersize=3.5,label='meshpoint x')
ax.set(title="with tol=0.00001",xlabel="time (t)", ylabel="y (x)")
plt.legend() 

#Remove the below portion if you don't want to see zoom in inset graph

axins = zoomed_inset_axes(ax,50 , loc=1) # zoom = 6
axins.plot(t, s,marker='o',markersize=2)
axins.set_xlim(2.47, 2.50) # Limit the region for zoom
axins.set_ylim(-2.0505, -2.0495)

plt.xticks(visible=False)  # Not present ticks
plt.yticks(visible=False)
#
## draw a bbox of the region of the inset axes in the parent axes and
## connecting lines between the bbox and the inset axes area
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.1")
plt.draw()


#plt.savefig('Q9(a).pdf',dpi=1000)
plt.show()



print("Meshpoint are so close that on graph it seems as a line, so either you reduce the desired accuracy(increase dx_max =0.01) to see clearly the distinct meshpoint or print the meshgrid array t")