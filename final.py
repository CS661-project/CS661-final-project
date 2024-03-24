import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
from st_aggrid import AgGrid
from raceplotly.plots import barplot
from collections import deque
import plotly.graph_objects as go
import plotly.express as px
import geopandas as gpd
import json
import math
from plotly.subplots import make_subplots

with st.sidebar:
    choose = option_menu("Main Menu", ["About", "Word Distribution","Cross sectional", "Country Specific"],
                         icons=['house', 'pin-map','bar-chart-steps','pin-map-fill'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#FFF3E2"},
        "icon": {"color": "#7C9070", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "color": "#7C9070", "font-weight": "bold"},
        "nav-link-selected": {"background-color": "#FEE8B0", 'color': '#7C9070', 'border-radius': '5px'},
    }
    )

logo = Image.open(r'logo.png')
if choose=='About':
    st.markdown(""" <style> .font {
        font-size:45px ; font-family: 'Comic Sans'; color: #cca300} 
        </style> """, unsafe_allow_html=True)

    st.markdown('<p class="font">CS661 Project</p>', unsafe_allow_html=True) 

elif choose=="Word Distribution":
    df = pd.read_csv('gdp_percapita_current_updated.csv')

    fig = go.Figure(data=go.Choropleth(
        locations = df['Country Code'],
        z = df['2018'],
        text = df['Country Name'],
        colorscale = 'Blues',
        autocolorscale=False,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_tickprefix = '$',
        colorbar_title = 'GDP<br>Billions US$',
    ))

    fig.update_layout(
        title_text='2018 Global GDP',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        annotations = [dict(
            x=0.55,
            y=0.1,
            xref='paper',
            yref='paper',
            text='Source: <a href="https://data.worldbank.org/indicator">\
                THE WORLD BANK</a>',
            showarrow = False
        )]
    )

    fig.update_layout(autosize=False,
                height=600,
                width=1000,
                margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig,use_container_width=True)

elif choose=="Cross sectional":
    year='2021'
    df1 = pd.read_csv('pop_tot_updated.csv')
    df = pd.read_csv('gdp_percapita_current_updated.csv')
    df=df.sort_values(by=year)

    df1 = df1.set_index('Country Name')
    df1 = df1.reindex(index=df['Country Name'])
    df1 = df1.reset_index()


    subfig = make_subplots(specs=[[{"secondary_y": True}]])

    fig = px.line(df, x="Country Name", y=year)
    fig2 = px.line(df1, x="Country Name", y=year)

    fig2.update_traces(yaxis="y2")

    subfig.add_traces(fig.data + fig2.data)
    subfig.layout.xaxis.title="Countries"
    subfig.layout.yaxis.title="Population"
    subfig.layout.yaxis2.title="GDP per capita"
    subfig.update_layout(
        title_text="Year: "+year,
    )

    subfig.for_each_trace(lambda t: t.update(line=dict(color=t.marker.color)))
    st.plotly_chart(subfig,use_container_width=True)

elif choose=="Country Specific":
    country='India'

    df1 = pd.read_csv('pop_tot_updated.csv')
    df1_t=df1.transpose()
    new_header = df1_t.iloc[0] 
    df1_t = df1_t[4:]
    df1_t.columns = new_header
    df1_t.index.name = 'year'
    df1_t.to_csv('update.csv')
    df1_t = pd.read_csv('update.csv')

    df = pd.read_csv('gdp_percapita_current_updated.csv')
    df_t=df.transpose()
    new_header = df_t.iloc[0] 
    df_t = df_t[4:]
    df_t.columns = new_header
    df_t.index.name = 'year'
    df_t.to_csv('update.csv')
    df_t = pd.read_csv('update.csv')

    subfig = make_subplots(specs=[[{"secondary_y": True}]])

    fig2 = px.line(df1_t, x='year', y=country)
    fig = px.bar(df_t, x="year", y=country)

    fig2.update_traces(yaxis="y2")

    subfig.add_traces(fig.data + fig2.data)
    subfig.layout.xaxis.title="Year"
    subfig.layout.yaxis2.title="Population"
    subfig.layout.yaxis2.title="GDP per capita"
    subfig.update_layout(
        title_text="Name: "+country,
    )
    st.plotly_chart(subfig,use_container_width=True)
