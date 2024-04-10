import plotly.express as px
import pandas as pd
import dash
from dash import Dash, dcc, Input, Output, html, callback, ctx
import json
import dash_echarts
from dash.exceptions import PreventUpdate
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


dash.register_page(__name__,order=3)

df_gdp = pd.read_csv('./Data_files/gdp_current_updated.csv')

layout = html.Div([
    html.H1('This is page 2'),
    html.Br(),
    dcc.Dropdown(
        options=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],
        value="2018",
        id="year_dropdown_pg2",
        style={"width": "40%"}
    ),
    dcc.Dropdown(
        options=[
            {'label': 'Population', 'value': 'pop_tot_updated'},
            {'label': 'Population Growth', 'value': 'pop_growth_updated'},
        ],
        value="pop_tot_updated",
        id="factor_pg2",
        style={"width": "40%"}
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Linear', 'value': 'Linear'},
            {'label': 'Log', 'value': 'Log'}
        ],
        value='Linear',
        id='xaxis-type',
        inline=True
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Linear', 'value': 'Linear'},
            {'label': 'Log', 'value': 'Log'}
        ],
        value='Linear',
        id='yaxis-type',
        inline=True
    ),
    dcc.Dropdown(
        options=[
            # {'label': 'None', 'value': None},
            {'label': 'OLS', 'value': 'ols'},
            {'label': 'Lowess', 'value': 'lowess'},
            # {'label': 'EWM', 'value': 'ewm'},
            # {'label': 'Rolling', 'value': 'rolling'}
        ],
        value=None,
        id='trendline-type',
        style={"width": "40%"}
    ),
    dcc.Graph(id="factor_vs_gdp")
])

@callback(
    Output("factor_vs_gdp","figure"),
    Input("year_dropdown_pg2","value"),
    Input("factor_pg2","value"),
    Input("yaxis-type","value"),
    Input("xaxis-type","value"),
    Input("trendline-type","value")
)
def generate_factor_vs_gdp(year_dropdown_pg2, factor_pg2, yaxis_type, xaxis_type, trendline_type):
    df_fact = pd.read_csv('./Data_files/' + factor_pg2 + '.csv')

    df_gdp_f = df_gdp[['Country Name', year_dropdown_pg2]]
    df_fact_f = df_fact[['Country Name', year_dropdown_pg2]]

    df_final = pd.merge(df_gdp_f, df_fact_f, on=['Country Name'])
    mask = df_final['Country Name'] == 'World'
    df_final = df_final[~mask]
    
    fig = px.scatter(df_final, x=year_dropdown_pg2 + '_x', y=year_dropdown_pg2 + '_y', hover_name='Country Name', trendline=trendline_type)
    fig.layout.xaxis.title = "GDP"
    fig.layout.yaxis.title = factor_pg2
    fig.update_yaxes(type='linear' if yaxis_type == 'Linear' else 'log')
    fig.update_xaxes(type='linear' if xaxis_type == 'Linear' else 'log')
    
    return fig
