import numpy as np
import sys

"""
Code profiling is a technique used to describe
how long and how often, various parts of a program
are executed. The beauty of a code profiler
is its ability to gather summary statistics
on individual pieces of our code.
"""

heroes = ['Batman','Superman','Wonder Woman']

hts = np.array([188.0, 191.0, 183.0])

wts = np.array([95.0, 101.0, 74.0])

def convert_units(heroes, heights, weights):

    """
    This function converts the height and weight list
    that are in centimeters and in kilograms to
    inches and pounds
    """
    new_hts = [ht * 0.3930 for ht in heights]
    new_wts = [wt * 2.204602 for wt in weights]

    hero_data = {}

    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

# We need to load the lineprofiler like this
# %load_ext line_profiler

# We must specify -f because convert_units 
# is a function
# %lprun -f convert_units convert_units(heroes,hts,wts)





