import numpy as np
import sys

"""
Here we will use CODE PROFILING to see the MEMORY usage of the
code
"""

def memory_usage_example():
    """
    In this example we will use the function getsizeof
    of the package "sys" to get the size of the variables
    nums_list.
    It must return the size of the object in bytes
    """
    nums_list = [*range(1000)]
    
    return sys.getsizeof(nums_list) 


from runtime_codeprof import convert_units

#%load_ext memory_profiler

heroes = ['Batman','Superman','Wonder Woman']

hts = np.array([188.0, 191.0, 183.0])

wts = np.array([95.0, 101.0, 74.0])

#%mprun -f convert_units convert_units(heroes,hts,wts)



