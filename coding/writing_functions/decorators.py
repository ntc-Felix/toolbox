"""
    A decorator is a wrapper that you can place around
a function that changes function's behavior.
    You can modify the inputs, the outputs or
even change the behavior of the function itself.

Decorators are used by assigning @ before its name
"""

@double_args
def multiply(a,b):
    return a*b

# Here @double_args modify the behavior of the multiply function
"""
 @double_args will be a decorator that multiplies every
 argument by two before passing them to the decorated
 function
  """

def multiply(a,b):
    return(a * b)
def double_args(func):
    return func

new_multiply = double_args(multiply)

new_multiply(1,5)

"""In order for your decorator to return a
modified function, it is usually helpful for it
to define a new function to return."""

# No decorator
def multiply(a,b):
    return a* b 
def double_args(func):
    # Define a new function that we can modify
    def wrapper(a,b):
        # For now, just call the unmodified function
        return func(a,b)
    # Return the new function
    return wrapper

new_multiply = double_args(multiply)
new_multiply(1,5) # will be 5
 
# With Decorator
def multiply(a,b):
    return a*b
def double_args(func):
    def wrapper(a,b)
    # Call the passed in function, but double each argument
    return func(a*2, b*2)
    return wrapper

new_multiply = double_args(multiply)
new_multiply(1,5) # will be 20

""" This time, instead of assigning the new function
to 'new_multiply', we're going to overwrite the
'multiply' variable"""

def double_args(func):
    def wrapper(a,b):
        return func(a*2, b*2)
    return wrapper

def multiply(a,b):
    return a*b

multiply = double_args(multiply)

multiply(1,5)

def double_args(func):
    def wrapper(a,b):
        return func(a*2, b*2)
    return wrapper

@double_args
def multiply(a,b):
    return a*b

multiply(1,5)

# The last 2 examples are exactly will have the exactly
# same result, but in the second we used a DECORATOR
