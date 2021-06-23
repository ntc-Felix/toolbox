import requests
import pandas as pd
from pandas.io.json import json_normalize


def api_requests_to_json(api_url,headers,params):
    """
    You will need to set the api_url,
    the headers and the params.
    This function will return a json object
    with data requested from an API
    """
    # Get data about NYC cafes from the Yelp API
    response = requests.get(api_url, 
                    headers=headers, 
                    params=params)

    return(response.json())

def api_requests_to_df(api_url, headers, params):
    """
    You will need to set the api_url,
    the headers and the params.
    This function will return a pandas DataFrame
    with data requested from the API
    """
    # Get data about NYC cafes from the Yelp API
    response = requests.get(api_url, 
                    headers=headers, 
                    params=params)

    # Extract JSON data from the response
    data = response.json()

    # Load data to a data frame
    df = pd.DataFrame(data)

    # View the data's dtypes
    return(df)

# Dealing with Nested JSON

def unnest(json_data,sep):
    """
    You will need to pass the argument json_data
    as a json file, and the separator of the
    json that are nested, to return a dataframe
    with both json arguments as columns
    """
    df = json_normalize(json_data,sep=sep)
    return(df)

def deeply_unnest(json_data, sep, item, path, columns):
    """
    You will need to pass the argument json_data
    as a json file,the separator of the
    jsons that are nested,
    item means the first argument of the outside
    nested json,
    path is the second argument and columns
    are the final arguments in the nest.
    This function will return a dataframe
    with all json arguments as columns
    """
    df = json_normalize(json_data[item],
        sep='_',
        record_path=path,
        sep=sep,
        meta=columns,
        meta_prefix='biz_')
    return(df)