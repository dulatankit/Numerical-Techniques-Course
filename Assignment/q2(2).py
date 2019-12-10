from scipy import optimize
import numpy as np

def f(x):
	return np.sin(np.cos(np.exp(x)))

def f1(x):
	return -np.exp(x)*np.cos(np.cos(np.exp(x)))*np.sin(np.exp(x))

root1=optimize.newton(f,-0.1,f1)
root2=optimize.newton(f,-1,f1)
print("\nroot with intial guess -0.1 is =",root1)
print("\n\nroot with intial guess -1 is =",root2)
print("\n\nvalue of function at ",root1," is ",f(root1))
print("\n\nvalue of function at ",root2," is ",f(root2))
print("\n\nwith different choice of inital guess we got differnt roots because it highly depends on curvature of the curve, for some functions even with slightly different initial guess one solution can be true but other may not even converge to any of the route")
