def add(x, y):
    """Adds x to y."""
    return x + y

def subtract(x, y):
    return y - x

def double(x):
    return add(x, x)

def square(x):
    return x*x

def displacement2(X, Y):
    return [subtract(Y[0], X[0]), subtract(Y[1], X[1])]

