"""
How SCOPE works in python?
    SCOPE determines which variables can be
    accessed at different points in your code.

Names are very useful things.
"""
x = 7
y = 200
print(x)

# What happens if we redefine x inside the function foo()?

def foo():
    x = 42
    print(x)
    print(y)

"""in foo() print() statement,
do we mean the x that equals 42 or the x thats
equals 7 ?
the answer is 42, because python understands
its a local value.

SCOPE:

Local > Nonlocal > Global > Built-in
"""


"""
In the first example we define a local variable
x and assigned the value of 200.
So when we call bar() it will print the value 200
but when we call print(x) it will print the value 10
which is an nonlocal value.

In the second example did the samething. But
when we defined the function bar() we called
the nonlocal value of x.
This means we change the value of the nonlocal x
which is the x value outside of the function bar()
"""
def foo():

    x = 10
    
    def bar():
        x=200
        print(x)

    bar()
    print(x)

foo()


def foo():

    x = 10
    
    def bar():
        nonlocal x
        x=200
        print(x)

    bar()
    print(x)

foo()