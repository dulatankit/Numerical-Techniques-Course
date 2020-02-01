from scipy import optimize
import numpy as np

def f(x):
	return np.sin(np.cos(np.exp(x)))
root=optimize.newton(f,-0.1)
print("\nroot is",root)
print("\n\nvalue of function at this root is=",f(root),"\n\n")
