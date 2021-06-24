import numpy as np

# using multiple lines
%%timeit
def runtime_example1():
    """
    if we want to optimize our python code
    we need to write the code in a way that we could
    run it in the less time as possible
    To do this we need to use the IPython built-in command "%timeit"
    One advantage in using %timeit is that it provides an average of timing statistics.
    Also %timeit needs to be runned outside this function
    To get the runtime of this entire function we need to
    use %%timeit before its definition, like we used here.
    """

    # this need to be runned outside of this function
    %timeit rand_nums = np.random.rand(1000)

    # here we save the runtime to a variable using "-o" after
    # the %timeit clause
    times = %timeit -o rand_nums = np.random.rand(1000)
    return times

# using multiple lines
%%timeit
def runtime_example2():

    """
    In this case we will use the clauses '-r'
    and '-n' to determine the number of runs and loops
    """
    %timeit -r2 -n10 rand_nums = np.random.rand(1000)
    # here we specified 2 runs and 10 loops

    rand_nums = np.random.rand(1000)
    return rand_nums


def runtime_example3():
    """
    built-in functions of the object "timeit"
    """

    times = %timeit -o rand_nums = np.random.rand(1000)

    times.timings # number of runs
    times.best # best time
    times.worst # worst time 


    
def comparing_runtime_example():

    """
    In this case we are comparing the creation of a
    formal dictionary using the formal syntax dict()
    and the creation of a literal dictionary {}
    """

    f_time = %timeit -o formal_dict = dict()
    l_time = %timeit -o literal_dict = {}

    diff = (f_time.average - l_time.average) * (10*9)

    return(print('l_time better than f_time by {} ns'.format(diff)))


