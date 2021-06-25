"""
Image that you are throwing a fancy party, and have hired
some caterers to provide refreshments for your guests.
Before the party starts, the caterers set up tables with food and drinks.
Then you and your friends dance, eat, and have a good time.
Whe the party is done, the caterers clean up the food and remove the tables.
In this analogy the caterers are like a context manager.

First they set up a context for your party, which was a room full of food and drinks.
Then they let you and your friends do whater you want.
Finally when the party is over, the caterers clean up and remove the context
that the party happened in.

1 - Set up a context
2 - Runm your code
3 - Remove the context

"""

with open('my_file.txt') as my_file:
    text = my_file.read()
    length = len(text)

print('The file is {} characters long'.format(length))

# here the context manager is open

# Using context manager will always look like this:

with <context-manager-function>(args):
    # Run your code here
    # This code is running "inside the context"

#This code runs after the context is removed. 



"""
    Here we will learn how to WRITE a context manager in python:
        - Class-based
        - Function-based

1) You need to define a function
2) Add any set up code you need
3) You must the keyword "yield" to signal Python that this is a special kind of function
4) Optional:
    Add any teardown code that you need to clean up the context
5) You must decorate the function with the "contextmanager" decorator from "contextlib" module.

"""

# Example:

@contextlib.contextmanager
def my_context():
    # Add any set up code you need
    yield
    # Add any teardown code you need


"""
The "yield" keyword:
    When you write this word, it means that you are going to return a value,
    but you expect to finish the rest of the function at some point in the future.
    The value that your context manager yields can be assigned to a variabile
    in the "with" statement by adding "as."

In the next example we've assigned the value 42 that my_context() yields to the variable "foo".
"""

@contextlib.contextmanager
def my_context():
    print('hello')
    yield '42'
    print('goodbye')

with my_context() as foo:
    print('foo is {}'.format(foo))


# Useful cases

@contextlib.contextmanager
def database(url):
    #set up database connection
    db = postgres.connect(url)

    yield db

    #tear down database connection
    db.disconnect()

url = 'http://datacamp.com/data'

with database(url) as my_db:
    course_list = my_db.execute(
        'SELECT * FROM courses'
    )
