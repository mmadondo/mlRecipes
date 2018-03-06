import numpy as np
from matplotlib import pyplot as plt
x0 = 0
y0 = 2
xf = 2
n = 101
deltaX = (xf - x0)/(n-1)
x = np.linspace(x0, xf, n)
y = np.zeroes([n]) #array y with n entries
y[0] = y0

for i in range(1, n):
    y[i] = deltaX*(-3*y[i-1] + 7*np.exp(4*x[i-1])) + y[i-1]

for i in range(n):
    print(x[i], y[i])
