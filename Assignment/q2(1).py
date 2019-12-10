from scipy import optimize
import numpy as np

def f(x):
	return np.sin(np.cos(np.exp(x)))

root=optimize.bisect(f,-1,1)
print("root of given non linear equation in (-1,1) interval is=",root)
print("value of function at the root we found is=",f(root))

print("\n\nvalue of the function at the obtained root is not zero because:\n1.This is an iterative method and doesn't give the exact roots\n2.Even if it is the true root it may not give zero because there is always be some roundoff error in evaluation the value of the function at the root")
