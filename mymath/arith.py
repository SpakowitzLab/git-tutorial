def add(x, y):
    """Adds x to y."""
    return x + y

def subtract(x, y):
    return x - y

def double(x):
    return add(x, x)

def square(x):
    return x*x

def displacement2(X, Y):
    return [subtract(X[0], Y[0]), subtract(X[1], Y[1])]

