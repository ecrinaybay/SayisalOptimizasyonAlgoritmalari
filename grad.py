import math
import numpy as np

def f(x):
    f = x[0]**2-x[1]**2+x[0]*x[1]
    return f

def gradf(x):
    gradf = [2*x[0]+x[1],-2*x[1]+x[0]]
    return gradf 

x = np.array([3,2])
print(f(x))
print(gradf(x))

epsilon = 0.001

for i in range(10):
    x = x + epsilon*np.array(gradf(x))
    print(f(x))