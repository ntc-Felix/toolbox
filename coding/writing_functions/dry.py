import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

# Dont Repeat Yourself (DRY)

# At the first moment we have a function like this:

def load_and_plot(path):
    """
    Load a data set and plot the first two principal components.

    Args:
        path (str): The location of a csv file.

    Returns:
        tuple of ndarray: (features, labels)
    """

    # load the data
    
    data = pd.read_csv(path)
    y = data['label'].values
    X = data[col for col in train.columns if col != 'label'].values

    pca = PCA(n_components = 2).fit_transform(X)
    plt.scatter(pca[:,0], pca[:,1])

    return X,y

# Here we want to split this function

def load_data(path):
    """
    Load a data set.
    
    Args:
        path(str): The location of a CSV file.

    Returns:
        tuple of ndarray: (features, labels)
    """

    data = pd.read_csv(path)
    y = data['labels'].values
    X = data[col for col in data.columns if col!= 'labels'].values
    
    return X,y

def plot_data(path):
    """
    Plot the first two principal components of a matrix.

    Args:
        X (numpy.ndarray): The data to plot 

    """

    pca = PCA(n_components=2).fit_transform()

    plt.scatter(pca[:,0], pca[:,1])

"""
Applying the steps to our code it becomes:
    -More flexible
    -More easily understood
    -Simpler to test
    -Simpler to debug
"""