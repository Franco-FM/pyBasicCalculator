#Basic calculator with python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def remainder(x, y):
    return x % y

def power(x, y):
    return x ** y

def square_root(x):
    return x ** 0.5

def cube_root(x):
    return x ** (1/3)

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

