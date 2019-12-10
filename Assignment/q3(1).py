from scipy.integrate import simps
from numpy import trapz

import numpy as np

def function(x):
    return np.exp(x)

x = np.arange(0,1,0.001)
y = function(x)

area = trapz(y,x)
print('\nIntegration value using trapz is: ',area,'\n')

# using Simpson's rule:

area = simps(y,x)
print('\nIntegration value using Simpson rule is: ',area,'\n')
