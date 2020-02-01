import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x=[0,1,2,3,4,5]
y=[1.0,2.0,1.0,0.5,4.0,8.0]
s=interpolate.lagrange(x,y)
x1=np.arange(0,5.1,0.1)
y1=s(x1)

plt.figure()
plt.plot(x,y,'ro',x1,y1,'g--')
plt.legend(['original','5th order polynomial'])
plt.title('lagrange interpolation')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.savefig('lagrange.png')
plt.show()
