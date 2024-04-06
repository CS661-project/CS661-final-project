# import plotly.express as px
# import pandas as pd
# import dash
# from dash import Dash, dcc, Input, Output, html, callback, ctx
# import json
# import dash_echarts
# from dash.exceptions import PreventUpdate
# import numpy as np
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots


# dash.register_page(__name__,order=4)


# with open('states_india.geojson') as response:
#     geodata = json.loads(response.read())

# fig_gl = px.choropleth_mapbox(
#                 df_refined, 
#                 geojson = geodata, 
#                 locations = df_refined.Districts, 
#                 color = df_refined[file], 
#                 color_continuous_scale = "YlGn",
#                 range_color = [max(df_refined[file]),min(df_refined[file])],
#                 featureidkey = "properties.District",
#                 mapbox_style = "carto-positron",
#                 center = {"lat": 22.5937, "lon": 82.9629},
#                 hover_name="STATE",
#                 hover_data=['STATE'],
#                 zoom = 3.0,
#                 # animation_frame = df_refined["Year"],
#                 )
# fig_gl.update_layout(autosize=False,
#             height=700,
#             width=1000,
#             margin={"r":0,"t":0,"l":0,"b":0},
#             )
# fig_gl.update_traces(marker_line_width=0.3)


# layout = html.Div([
#     html.H1('This is our India Specific page'),
#     html.Br(),
    
#     dcc.Graph(id="ind_map"),
# ])