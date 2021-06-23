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
    
%load_ext memory_profiler

%mprun runtime_codeprof.py

from ru

