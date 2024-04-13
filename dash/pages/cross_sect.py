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


dash.register_page(__name__,order=5)

@callback(
        Output("cross_sect", "figure"),
        [Input("year_dropdown","value")]
)
def generate_cross_sect(year_dropdown):
    year='2021'
    df1 = pd.read_csv('../pop_tot_updated.csv')
    df = pd.read_csv('../gdp_percapita_current_updated.csv')
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
    return subfig

layout = html.Div([
    html.H1('This is our Cross Sectional page'),
    html.Br(),
    dcc.Dropdown(
                options=['No','2021'],
                value="NO CHOOSEN",
                id="year_dropdown",
                style={"width": "40%"}
            ),
    dcc.Graph(id="cross_sect")
])