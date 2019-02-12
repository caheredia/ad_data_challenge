import pandas as pd
import numpy as np

def rank_ctr(data, region):
    '''Rank keywords by CTR in descending order.

    Groups by keyword and takes the mean of CTR values.
    Sorts dataframe by CTR values.

    Parameters
    ----------
    data : pandas.DataFrame
        dataframe to modify
    region : string
        country of interest

    Returns
    -------
    df : pandas.DataFrame
    Sorted dataframe with keywords sorted by CTR.
    '''
    df = (data[data['country'] == region]
          .groupby('keyword')[['CTR']]
          .agg('mean')
          .sort_values(by='CTR', ascending=False))
    return df


def rank_cpc(data, region):
    '''Rank keywords by CPC in ascending order.

    Function groups by keyword and takes the mean of CPC values.
    Sorts dataframe by CTR values.

    Parameters
    ----------
    data : pandas.DataFrame
        dataframe to modify
    region : string
        country of interest

    Returns
    -------
    df : pandas.DataFrame
    Sorted dataframe with keywords sorted by CPC.
    '''
    df = (data[(data['country'] == region)]
          .groupby('keyword')[['CPC']]
          .agg('mean')
          .sort_values(by='CPC'))
    return df

def common_keywords(data, region, first_index=0, last_index=10):
    '''Finds the common word in CTR and CPC.

    Call rank_ctr and rank_cpr functions to find ranked keywords.
    Converts lists to sets to find intersection of sets. 

    Parameters
    ----------
    data : pandas.DataFrame
        dataframe to modify
    region : string
        country of interest
    first_index : integer (optional)
        beginning of slice
    last_index : integer (optional)
        end of slice

    Returns
    -------
    top : list
    List containing intersection of keywords for CTR and CPC.
    '''
    df_ctr = rank_ctr(data, region)
    df_cpc = rank_cpc(data, region)
    top_ctr = list(df_ctr.index[first_index:last_index])
    top_cpc = list(df_cpc.index[first_index:last_index])
    top = list(set(top_ctr) & set(top_cpc))
    return top