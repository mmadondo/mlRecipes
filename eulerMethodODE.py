"""
Author: Malvern Madondo
Created: Feb 20, 2018
"""
from __future__ import division
import numpy as np

def f(x):
    return 1-x

#initial conditions
x0 = 0

#time step
dt = 0.01

#solve the DE from 0 to time T
T = 5

#define discretized time; assume dt divides exactly into T
t = np.linspace(0, T, int(T/dt)+1)

#array to store the solutions
x = np.zeros(len(t))

#integrate the DE using Euler's Method
x[0] = x0
for i in range(1, len(t)):
    x[i] = x[i-1] + f(x[i-1])*dt

#save the solution
np.savetxt('t.txt', t)
np.savetxt('x.txt', x)

'''
Sources:
1. http://connor-johnson.com/2014/02/21/numerical-solutions-to-odes/
2. http://www.nervouscomputer.com/hfs/pdf/introtns/Getting-to-know-Python.pdf
3. http://hplgit.github.io/prog4comp/doc/pub/p4c-sphinx-Python/._pylight005.html
4. http://code.activestate.com/recipes/577647-ode-solver-using-euler-method/
'''
