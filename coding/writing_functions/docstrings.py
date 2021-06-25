import pandas as pd
import numpy as np


def split_and_stack(df,new_names):
    """
    Split a DataFrame's columns into two halves and then stack them vertically,
    returning a new DatafFrame with 'new names' as the column names.
    
    Args:
        df (DataFrame): The DataFrame to split
        new names (iterable of str): the column names for the new DataFrame

    Returns:
        DataFrame

    Raises:
    """

    half = int(len(df.columns)/2)
    left = df.iloc[:, :half]
    right = df.iloc[:,half:]

    return pd.DataFrame(data = np.vstacks([left.values, right.values], columns = new_names))

def function(args):
    """
    Description of what the function does
    
    Args:
        arg1 (type of arg): what is this arg
        arg2 (type of arg): what is this arg
        
    Returns:
        Type of data: what is this data

    Raises:
        Possible erros: why this errors pop-ups on the screen
    """

# to see the documentation of a function you must do: function.__doc__
# or import inspect -> than inspect.getdoc(function)