"""
Here we will apply different python built-in functions
for different situations
"""
def enumerate_example_1():

    """  this will return a list of tuples
     each tuple will contain 2 indexes
     the first will be the number of the letter
     and the second will be the letter itself """

    # Using ENUMERATE
    # creating a list of letters
    letters = ['a','b','c','d']

    # applying enumerate to this list
    indexed_letters = enumerate(letters)
    # this will return an "enumerate object"

    # turning the enumarate object into a list
    indexed_letters_list = list(indexed_letters)


    return(indexed_letters_list)

def enumerate_example_2():

    """ this will return a list of tuples
     each tuple will contain 2 indexes
     the first will be the number of the letter
     and the second will be the letter itself
     but this time, because of the "start" ARG
     the counting will start at 5 and so on"""
    
    # Using "stats" argument of ENUMERATE
    # creating a list of letters
    letters = ['a','b','c','d']

    # applying enumerate to this list AND START
    indexed_letters = enumerate(letters,start=5)
    # this will return an "enumerate object"

    # turning the enumarate object into a list
    indexed_letters_list = list(indexed_letters)

    return(indexed_letters_list)

def map_example():

    """
    This function is an use case for the built_in
    function "map", here we want to apply the function
    round to a list of float.
    
    It will return the list of the rounded list of floats
    """

    # Creating a list of float args
    nums = [1.5,2.3,3.4,4.6,5.0]

    # Now we are going to apply the built_in function
    # "ROUND" to the list "nums"
    rnd_nums = map(round,nums)

    # We need to set rnd_nums as a LIST
    # because it is "map" object, it's the same case
    # when we used it with "enumerate"
    return(list(rnd_nums))


def enumerate_example3():

    """
    This example we use the "*" to unpack the
    arguments inside the enumerate object
    this is a simplier way to apply the examples 1 and 2.
    """
    names = ['Marlon','Saura','Félix','Rozindo']
    # Unpack an enumerate object with a starting index of one
    indexed_names_unpack = [*enumerate(names, start=1)]
    return(indexed_names_unpack)


def map_example2():

    """
    This is a smart way to use map to
    UPPER CASE the elements of a list
    """
    names = ['Marlon','Saura','Félix','Rozindo']

    # Use map to apply str.upper to each element in names
    names_map  = map(str.upper, names)

    # Unpacking the MAP object
    return([*names_map])