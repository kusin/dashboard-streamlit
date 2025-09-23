# library ui-dashboard
import streamlit as st;

# library manipulation array
import numpy as np;

# library manipulation dataset
import pandas as pd;

## library data visualization
import seaborn as sns
import matplotlib.pyplot as plt

# call method from other file
from streamlit_data_exploratory import *
from streamlit_data_visualization import *

# config web streamlit
st.set_page_config(page_title="My Dasboard", layout="wide")

# config load dataset
dataset = get_dataset()
df_name = grouping_sales(dataset, "Name")
df_platform = grouping_sales(dataset, "Platform")
df_genre = grouping_sales(dataset, "Genre")
df_publisher = grouping_sales(dataset, "Publisher")

# container-header
with st.container():
    st.markdown("## Data Science - Exploratory Data Analysis of Video Games Sales")
    st.markdown("- Created By. Aryajaya Alamsyah, Nov 2023 (link download on https://www.kaggle.com/datasets/gregorut/videogamesales)")
    st.markdown("<br>", unsafe_allow_html=True)

# container-body
with st.container():
    st.dataframe(dataset, use_container_width=True)

# container-body
st.success("")
with st.container():

    # create two columns
    col1, col2 = st.columns(2, gap="medium")

    # Best game-name in each region
    with col1:
        st.error("Best game-name of video games sales")
        st.dataframe(df_name, use_container_width=True)

    # Best platform in each region
    with col2:
        st.error("Best platform of video games sales")
        st.dataframe(df_platform, use_container_width=True)
    
    # Best genre in each region
    with col1:
        st.error("Best genre in each region")
        st.dataframe(df_genre, use_container_width=True)
    
    # Best publisher in each region
    with col2:
        st.error("Best publisher in each region")
        st.dataframe(df_publisher, use_container_width=True)

# container-body
st.success("")
with st.container():

    # create two columns
    col1, col2 = st.columns(2, gap="medium")
    
    with col1: # Barplot for Best game-name in each region
        st.error("Best game-name in each region")
        st.plotly_chart(barplot(
            data=df_name, x="Name", y="Global_Sales", title="Top 4 games based on global sales", x_title="Game Name", y_title="Sum of Global Sales"
        ))
    
    with col2: # Barplot for Best platform in each region
        st.error("Best platform in each region")
        st.plotly_chart(barplot(
            data=df_platform, x="Platform", y="Global_Sales", title="Top 4 platform based on global sales", x_title="Platform Name", y_title="Sum of Global Sales"
        ))

    with col1: # Barplot for Best genre in each region
        st.error("Best genre in each region")
        st.plotly_chart(barplot(
            data=df_genre, x="Genre", y="Global_Sales", title="Top 4 genre based on global sales", x_title="Genre Name", y_title="Sum of Global Sales"
        ))

    with col2: # Barplot for Best publisher in each region
        st.error("Best publisher in each region")
        st.plotly_chart(barplot(
            data=df_publisher, x="Publisher", y="Global_Sales", title="Top 4 publisher based on global sales", x_title="Publisher Name", y_title="Sum of Global Sales"
        ))
    st.success("")