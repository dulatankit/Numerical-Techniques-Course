from scipy.integrate import romberg

from scipy.integrate import quad
import numpy as np

def function(x):
    return np.exp(x)
area = romberg(function,0,1)
print('\nIntegration value using romberg is: ',area)

area = quad(function,0,1)
print('\n\nIntegration value using guassian quadrature is: ',area,'\n')
