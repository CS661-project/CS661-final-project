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


dash.register_page(__name__,order=2)


global global_k
global_k='Filter'

@callback(
        Output("settings_store","data"),
        Input("settings_dropdown","value"),
)
def generate_settings_store(settings_dropdown):
    print('i m in: ',settings_dropdown)
    global global_k
    global_k=settings_dropdown
    return settings_dropdown

layout = html.Div([
    dcc.Store(id='settings_store'),
    dcc.RadioItems(
        options=[
            {'label': 'Filter', 'value': 'Filter'},
            {'label': 'No Filter', 'value': 'No Filter'}
        ],
        value='Filter',
        id='settings_dropdown',
        inline=True
    ),
    html.Br(),
    dcc.Slider(
        id='settings_slider',
        min=1,
        max=10,
        step=1,
        value=5,
    ),
], className="page1_style")

