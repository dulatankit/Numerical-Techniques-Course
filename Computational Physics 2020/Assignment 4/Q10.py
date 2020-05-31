# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:33:04 2020

@author: Ankit Dulat
"""

import numpy as np
import matplotlib.pyplot as plt
import emcee
from scipy.optimize import minimize
import corner
import matplotlib.backends.backend_pdf as pf  

#Reading data from the file
data=np.loadtxt('data10.txt',delimiter='&')
x=data[:,1]
y=data[:,2]
yerr=data[:,3] 

#logarithm of PDF of the data for given model (return a number(probability))
def log_L(theta,x,y,yerr):   #make sure everywhere in the code to use same convention of writting the fitting parameters as 1st argument
    a,b,c = theta
    model = a*x*x + b*x + c 
    sigma2 = yerr**2
    return (0.5*np.sum((y-model)**2/sigma2 + np.log(2*np.pi*sigma2)))
# Logarithm of prior PDF (inital guess of fitting parameters or any other initial information) 
def log_prior(theta):
  a,b,c = theta
  if -500.0 < a < 500.0 and -200 < b < 200.0 and -500 < c < 500:
    return 0.0
  return -np.inf
# Required Logarithm of post PDF i.e. probability distribution of model parameters for the given data
def log_P(theta,x,y,yerr):
    lp= log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp - log_L(theta,x,y,yerr)

guess = (1.0,1.0,1.0)
soln = minimize(log_L,guess,args=(x,y,yerr))  #To get the initial good guess (which maximise the post PDF) for the MCMC sampling code
#sol contains the fitting paramets for which post PDF is maximum

# numbers of random chains we want to create (to genrate large no. of random no.) & no. of fitting parameters resp.
nwalkers, ndim = 50,3

pos = soln.x + 1e-4*np.random.randn(nwalkers,ndim)    #pos is array containing good guess of fitting parameters for all random chains
#print(pos)

sampler = emcee.EnsembleSampler(nwalkers,ndim,log_P,args=(x,y,yerr))   #These 2 lines sample the unnormalised post PDF using MCMC
sampler.run_mcmc(pos, 4000)

pm=pf.PdfPages("Q10.pdf")   #To save all graph in same pdf
plt.figure(figsize=(8,8))

plt.subplot(311)
plt.title("50 Random chains for each parameter")
plt.plot(sampler.chain[:,:,0].T,'-', color='k', alpha=0.3)  #Sampler.chain[nwalkers,N,ndim] contain sampled data for all 50 chains for N=4000 points and for all fitting parametrs(ndim)
plt.ylabel('a')
plt.subplot(312)
plt.plot(sampler.chain[:,:,1].T,'-', color='k', alpha=0.3)
plt.ylabel('b')
plt.subplot(313)
plt.plot(sampler.chain[:,:,2].T,'-', color='k', alpha=0.3)
plt.xlabel('step number')
plt.ylabel('c')
plt.tight_layout()
pm.savefig()
plt.show()


medians = np.median(sampler.flatchain,axis=0)   #flatchain concatens all 50 chains is 1 so sampler.flatchain is [N][ndim] dimensional
a_true, b_true,c_true = medians

labels=["a","b","c"]

fig = corner.corner(sampler.flatchain,labels=labels,truths=(a_true,b_true,c_true))
pm.savefig()
plt.show()

#calculating 1*sigma deviation

print("Parameter\tBest-fit value\t\tsigma+\t\t\tsigma-")
L=['a','b','c']
for i in range(ndim):
    pmt = np.percentile(sampler.flatchain[:,i],[16,50,84])   #pmt contains 3 value for 3 percentile
    fin = np.diff(pmt)
    print(L[i],'\t',pmt[1],'\t',fin[1],'\t',-fin[0])
    

#for plotting the best fit curve for 200 random values of fitted parameter from posterior PDF   
index=np.argsort(x)
for i in range(200):
    a=np.random.randint(0,200)
    a1 ,b1,c1 = sampler.flatchain[a,:]
    f1=a1*x*x+b1*x+c1
    plt.plot(x[index],f1[index],c='yellow')
plt.plot(x[index],f1[index],c='yellow',label='200 Models')
plt.errorbar(x,y,yerr,fmt='o',capsize=3.5,mfc='red',ecolor='k',label='data')

f=a_true*x*x+b_true*x+c_true
plt.errorbar(x,y,yerr,fmt='o',capsize=3.5,mfc='red',ecolor='k')
plt.plot(x[index],f[index],c='green',label='Best-fit Model')
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Data fitted with 200 models")
plt.legend()
pm.savefig()
plt.show()
pm.close()