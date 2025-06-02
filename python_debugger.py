import pdb

def add(x,y):
    pdb.set_trace()
    return x+y

# add(5,6)

def buggy_function():
    a = 10
    b = 0
    pdb.set_trace()
    c = a/b
    return c

# buggy_function()

def greet(name):
    message = 'Hello ' + name
    pdb.set_trace()
    return message

greet('raj')