"""
Here we will talk about decorators and where are they useful

Fundamental concepts:
    Functions are just another type of object

Python Objects:
    def x():
        pass
    x = [1,2,3]
    x = {'foo':42}
    x = pandas.DataFrame()
    x = 'this is a sentence'
    x = 3
    x = 71.2
    import x

When you type 'my_function' without the parentheses,
you are referencing the function itself.
When you type 'my_function()' you are calling its value
"""
def my_function():
    print('hello world')

list_of_functions = [my_function, open, print]

list_of_functions[2]('i am printing with an element of a lista')

dict_of_functions = {
    'func1': my_function,
    'func2': open,
    'func3': print
}

dict_of_functions['func3']('i am printing with a value of a dict')

"""
Since a function is just an object like anything else in Python,
you can pass one as an argument to another function.
In this next example we will pass 2 functions :
yes and no as arguments
of the function has_docstring.

Since the no() function doesn't have a docstring, the has_docstring()
function returns False.
Likewise, has_docstring() returns True for the yes() function
"""

def has_docstring(func):
    """
    Check to see if the function 'func'
    has a docstring.
    
    Args:
        func (callable): A function.

    Returns:
        bool
    """

    return func.__doc__ is not None


def no():
    return 42

def yes():
    """Return the value 42"""
    return 42

has_docstring(no)
has_docstring(yes)

# Defining a function inside another function

def foo():
    x = [3,6,9]

    def bar(y):
        print(y)
    
    for value in x:
        bar(x)

# Why defining a function inside another function is useful?
# Example

def foo(x,y):
    if x > 4 and x < 10 and y > 4 and y < 10:
        print(x*y)

def foo(x,y):
    def in_range(v):
        return v > 4 and v < 10 

    if in_range(x) and in_range(y):
        print(x*y)

# here we can clearly see that the seconde example is way more readable

