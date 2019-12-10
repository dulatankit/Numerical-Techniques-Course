import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x=[0,1,2,3,4,5]
y=[1.0,2.0,1.0,0.5,4.0,8.0]
c=interpolate.InterpolatedUnivariateSpline(x,y,k=3)
s=interpolate.InterpolatedUnivariateSpline(x,y,k=2)
l=interpolate.InterpolatedUnivariateSpline(x,y,k=1)
x1=np.arange(0,5.1,0.1)
y1=l(x1)
y2=s(x1)
y3=c(x1)

plt.plot(x,y,'ro',x1,y1,'g--',x1,y2,'b--',x1,y3,'y--')
plt.legend(['data','Linear Spline','Quadratic spline','Cubic Spline'])
plt.title('Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('spline.png')
plt.show()
