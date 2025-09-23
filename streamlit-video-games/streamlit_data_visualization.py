# library ui-dashboard
import streamlit as st;

# library manipulation dataset
import pandas as pd;

# library manipulation array
import numpy as np;

# library data visualization
import plotly.express as px;
import plotly.graph_objects as go;

# function for create barplot
def barplot(data, x, y, title, x_title, y_title):
    
    fig = px.bar(data_frame=data, x=x, y=y, text_auto='.3s')

    fig.update_traces(
        marker_color = px.colors.diverging.RdYlBu,
        textposition='outside'
    )

    fig.update_layout(
        title = title,
        xaxis_title = x_title,
        yaxis_title = y_title,
        xaxis=dict(tickangle=0),
        yaxis=dict(tickangle=0),
    )

    return fig