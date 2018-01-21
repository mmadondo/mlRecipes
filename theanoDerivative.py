# computing gradients using Theano: http://deeplearning.net/software/theano/tutorial/gradients.html
#Example 1: To find the derivative of y = x**2 + 3*x or x-squared plus 3x

import numpy
import theano
import theano.tensor as T
from theano import pp

x = T.dscalar('x')
y = x**2 + 3*x
gy = T.grad(y, x)
pp(gy)  # print out the gradient prior to optimization
f = theano.function([x], gy)
f(4)
