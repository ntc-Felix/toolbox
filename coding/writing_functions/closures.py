"""
A CLOSURE in python is a tuple of variables that are
no longer in SCOPE, but that a function
needs in order to run.
"""
# Example

def foo():
    a = 5
    def bar():
        print(a)
    return bar

func = foo()

func()

"""
here we could think that 'a' would not be
observable outside of the scope of foo().
That's where closures come in.
When foo() returned the new bar() function,
Python helpfully attached any nonlocal
variable that bar() was going to need
to the function object.

Those variables get stored in a tuple in the
"__closure__" attribute of the function.
You can view the value of that variable by
acessing the "cell_contents" of the item"""

func.__closure__[0].cell_contents


# using del()

x = 25

def foo(value):
    def bar():
        print(value)
    return bar

my_func = foo(x)
my_func()

# The result will be 25, but what happens if
# we use del(x) and call this function again?

del(x)
my_func()
# it will return 25 in the same way, why this happens?

"""
This happens because foo()'s 'value'argument
gets added to the CLOSURE attached to the new
my_func function. So even though x doesn't
exist anymore, the value persists in its closure.
"""
my_func.__closure__[0].cell_contents

