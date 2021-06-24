import pandas as pd
import numpy as np

"""
.iterrows() returns each DataFrame
row as a tuple of (index, pandas Series) pairs.
Here we will use this tool to understand its
use cases
"""

col1 = ['PIT','PIT','PIT','PIT','PIT']
col2 = ['NL','NL','NL','NL','NL']
col3 = [2012, 2011, 2010, 2009, 2008]
col4 = [651, 610, 587, 636, 735]
col5 = [674, 712, 866, 768, 884]
col6 = [79, 72, 57, 62, 67]
col7 = [162, 162, 162, 161, 162]
col8 = [0, 0, 0, 0, 0]

pit_df = pd.DataFrame()

pit_df['Team'] = col1
pit_df['League'] = col2
pit_df['Year'] = col3
pit_df['RS'] = col4
pit_df['RA'] = col5
pit_df['W'] = col6
pit_df['G'] = col7
pit_df['Playoffs'] = col8

#dataframe that we will use for examples
baseball_df = pd.read_csv(r'C:\Users\T-Gamer\Documents\GitHub\tools\toolbox\engineeringtoolbox\baseball_df.csv')


def iterrows_example():
    # Iterate over pit_df and print each row
    lista = []
    for i,row in pit_df.iterrows():
        lista.append(row)
    # each row is stored as a panda.series
    return(lista)

def itertuples_exaple():
    """ Iterate over pit_df and get each row as
    a named_tuple
    namedtuple have helpfull methods like
    namedtuple.columnname
    itertuples is faster than iterrows
    """
    lista = []

    for i,row in pit_df.itertuples():
        lista.append(row)
        # each row is stored as a panda.series
    return(lista)

def apply_example():
    """
    One alternative to using a loop to iterate over
    a DataFrame is to use pd.apply()
    This function takes a funcation as an input
    and applies this function to an entire dataframe
    We must specify an axis that we'd like our function
    to act on.
    Axis = 0 apply our function to columns
    Axis = 1 apply our function to rows
    It can be used with lambda functions
    """

    # ilustrative example
    baseball_df.apply(
        lambda row: function(arg1,arg2),axis=1
    )

def to_numpy_examples():
    """
    In terms of speed when we want to calculate something
    between 2 columns in pandas
    we will prefer to use df['col'].to_numpy()
    insted of df['col'], because the first method is
    much faster than the second one
    """

# Speed order
# numpy arrays >> .itertuples() >> .apply()