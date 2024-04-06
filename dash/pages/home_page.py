import dash
from dash import Dash, dcc, Input, Output, html,callback

dash.register_page(__name__,order=1,path='/')

layout = html.Div([
    html.H1('CS661 Project'),
])