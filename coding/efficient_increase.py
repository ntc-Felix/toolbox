from collections import Counter
from itertools import combinations


names = ['Bulbasaur','Charmander','Squirtle']
hps = [45, 39, 44]

combined = []

# Combining objects using "for"
for i,pokemon in enumerate(names):
    combined.append((pokemon,hps[i]))

print(combined)


#Combining objects using zip

combined_zip = zip(names, hps)

[*combined_zip]


# Counting with loop
poke_types = ['Grass', 'Dark','Fire','Fire','Water']

type_counts = {}
def counting_example():

    """
    In this function we want to count how many times
    each element of the list poke_types appears
    To do this we are going to use for loop
    """
    for poke_type in poke_types:
        if poke_type not in type_counts:
            type_counts[poke_type] = 1
        else:
            type_counts[poke_type] +=1
    
    return type_counts

def counting_example2():

    """
    In this function we want to count how many times
    each element of the list poke_types appears
    To do this we are going to collection.Counter()
    """

    # from collections import Counter was already write in this code

    type_counts = Counter(poke_types)
    
    return type_counts


def combinations_examples():

    """
    This function returns the number of possible combinations
    with a tuple of 2 elements using a list of 5 elements
    """
    poke_types = ['Bug','Fire','Ghost','Grass','Water']
    combos=[]

    for x in poke_types:
        for y in poke_types:
            if x == y:
                continue
            if((x,y) not in combos) & ((y,x) not in combos):
                combos.append((x,y))
    
    return(combos)

def combinations_example2():
    """
    This function returns the number of possible combinations
    with a tuple of 2 elements using a list of 5 elements
    But this time we are going to use the function combinations()
    from itertools module
    """

    # from itertools import combinations already write in this code

    poke_types = ['Bug','Fire','Ghost','Grass','Water']
    combos_obj = combinations(poke_types,2)

    return [*combos_obj]



# Using "SET"

"""
SET THEORY:
the built-in datatype 'set' is used to compare 2 or more lists/arrays
it has 4 built-in functions:
    intersection(): all elements that are in both sets
    difference(): all elements in one set but not the other
    symmetric_difference(): all elements in exactly one set of
    union(): all elementes that are in either set
set is a very important tool to check if a value exists in
a sequence or not using the "in" operator
"""

def comparing_example():

    """
    This example shows how set is used to compare lists
    We will get the intersection between the 2 lists as an output

    """

    list_a = ['Bulbasaur','Charmander','Squirtle']
    list_b = ['Caterpie','Pidgey','Squirtle']

    set_a = set(list_a)
    set_b = set(list_b)

    return set_a.intersection(set_b)

def comparing_example2():

    """
    This example shows how set is used to compare lists.
    We will get the difference between the 2 lists as an output
    """

    list_a = ['Bulbasaur','Charmander','Squirtle']
    list_b = ['Caterpie','Pidgey','Squirtle']

    set_a = set(list_a)
    set_b = set(list_b)

    return set_a.difference(set_b)

def comparing_example3():

    """
    This example shows how set is used to compare lists
    Here we will get all the elements that appears in both lists
    """

    list_a = ['Bulbasaur','Charmander','Squirtle']
    list_b = ['Caterpie','Pidgey','Squirtle']

    set_a = set(list_a)
    set_b = set(list_b)

    return set_a.union(set_b)

def comparing_example4():

    """
    This time we are going to use set to get the
    UNIQUE elements in a list
    """

    primary_types = ['Grass','Psychic','Dark','Bug',
                    'Grass','Psychic','Dark','Bug',
                    'Grass','Psychic','Dark','Bug',
                    'Grass','Psychic','Dark','Bug',
                    'Grass','Psychic','Dark','Bug',
                    'Grass','Psychic','Dark','Bug']

    unique_types_set = set(primary_types)

    return([*unique_types_set])

