import plotly.express as px
import pandas as pd
from dash import Dash, dcc, Input, Output, html, callback, ctx
import json
import dash_echarts
from dash.exceptions import PreventUpdate
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

app = Dash(__name__)
# app.config.suppress_callback_exceptions=True
app.layout = html.Div(children=[
    html.Div(className="row", children=[

        html.Div(className="six columns", children=[
            dcc.Dropdown(
                options=["About", "Word Distribution","Cross sectional", "Country Specific"],
                value="About",
                id="dataframe_dropdown",
                style={"width": "40%"}
            )
        ])
    ]),

    html.Br(),
    html.Div(id="img")
])

def generate_abt():
    h1=html.Div("CS661 Project")
    return h1

def generate_world_dist():
    df = pd.read_csv('../gdp_percapita_current_updated.csv')

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
    return dcc.Graph(id="world_map",figure=fig)

def generate_cross_sect():
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
    return dcc.Graph(id="cross_map",figure=subfig)

def generate_country_specific():
    country='India'

    df1 = pd.read_csv('../pop_tot_updated.csv')
    df1_t=df1.transpose()
    new_header = df1_t.iloc[0] 
    df1_t = df1_t[4:]
    df1_t.columns = new_header
    df1_t.index.name = 'year'
    df1_t.to_csv('update.csv')
    df1_t = pd.read_csv('update.csv')

    df = pd.read_csv('../gdp_percapita_current_updated.csv')
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
    return dcc.Graph(id="country_map",figure=subfig)


@app.callback(
    Output("img", "children"),
    Input("dataframe_dropdown", "value")
)
def update(dataframe_dropdown):
    if dataframe_dropdown=="About":
        return generate_abt()
    elif dataframe_dropdown=="Word Distribution":
        return generate_world_dist()
    elif dataframe_dropdown=="Cross sectional":
        return generate_cross_sect()
    else:
        return generate_country_specific()


if __name__ == "__main__":
    app.run_server(debug=True)
