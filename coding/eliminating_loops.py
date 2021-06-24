"""
When we use loops like
for, while or nested loops we are using more memory
and it costs more time to run
"""

poke_stats = [[90,92,75,60],
              [25,20,15,90],
              [65,130,60,75],
              [65,130,60,75]]

def loop_example():

    """
    Here we will calculate the sum of the rows
    in poke_stats
    """

    totals = []

    for row in poke_stats:
        totals.append(sum(row))
    
    return(totals)

def eliminating_loop_example():

    """
    Here we will calculate the sum of the rows
    in poke_stats but using list comprehension
    """

    totals_comp = [sum(row) for row in poke_stats]

    return(totals_comp)

def totals_map():

    """
    Now the same example using map()
    """
    totals_map = [*map(sum,poke_stats)]

    return(totals_map)

    