import time

def timer(func):
    """ 
    A decorator that prints how long a function took to run.
    
    Args:
        func (callable): the function being decorated.
        
    Returns:
        callable: The decorated function.
    """
    # Define the wrapper function to return
    def wrapper(*args, **kwargs):
        # When wrapper() is called, get the current time
        t_start = time.time()
        # Call the decorated function and store the result.
        result = func(*args, **kwargs)
        # Get the total time it took to run, and print it.
        t_total = time.time() - t_start
        print('{} took {}s'.format(func.__name__, t_total))

        return result

    return wrapper

# example
@timer
def sleep_n_second(n):
    time.sleep(n)

sleep_n_second(5)

def memoize(func):
    """Store the results of decorated function
    for last lookup
    """
    cache = {}
    # Store results in a dict that maps arguments to results
    def wrapper(*args, **kwargs):
        if(args, kwargs) not in cache:
            # call func() and store the result.
            cache[(args,kwargs)] = func(*args,**kwargs)
            return cache[(args,kwargs)]
    return wrapper

@memoize
def slow_function(a,b):
    print('Sleeping ... ')
    time.sleep(5)

    return a + b

slow_function(3,4)

"""
When to use decorators
    Add common behavior to multiple functions
    
"""