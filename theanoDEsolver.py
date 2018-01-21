import numpy
import theano

# the right-hand side
def f(x, t):
    return x*(1-x)

x = theano.tensor.matrix() # why not a matrix
dt = theano.tensor.scalar()
t = theano.tensor.scalar()

x_next = x + f(x, t)*dt # implement your favourite RK method here!

# matrix of random initial values
# store it on the device
x_shared = theano.shared(numpy.random.rand(10, 10))

step = theano.function([t, dt], [],
        givens=[(x, x_shared)],
        updates=[(x_shared, x_next)],
        on_unused_input='warn')

t = 0.0
dt = 0.01

while t < 10:
    step(t, dt)
    t += dt
    # test halt condition here

print(x_shared.get_value()) # read back the result
