# library ui-dashboard
import streamlit as st;

# library manipulation dataset
import pandas as pd;

# library manipulation array
import numpy as np;

# define function
def get_dataset():

    # load dataset
    df = pd.read_csv("../dataset/vgsales_after_smoothing.csv")
    
    # return values
    return df

# define function
def grouping_sales(dataset, columns):

    # process grouping
    df = dataset.groupby(columns)[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].aggregate("sum").reset_index()

    # sorting values
    df = df.sort_values(by=["Global_Sales"], ascending=False).head(5)

    # return values
    return df