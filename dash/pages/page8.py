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
        Output("factor_pg8","options"),
        Input("year_dropdown_pg8","value"),
)
def change_options(year_dropdown_pg8):
    from pages import settings
    return settings.global_options


@callback(
        Output("parallel_coordinate", "figure"),
        [Input("year_dropdown_pg8","value"),
         Input("factor_pg8","value")
        ]
)
def generate_parallel_coordinate(year_dropdown_pg8,factor_pg8):
    if year_dropdown_pg8==None:
        return html.Br()
    if type(factor_pg8)==str:
        return html.Br()
    print(factor_pg8)
    l=['Country Name', 'Country Code']
    df_final = pd.read_csv('income_cat.csv')

    for fact in factor_pg8:
        df_fact = pd.read_csv('./Data_files/' + fact + '.csv')
        df_fact = df_fact.drop(['2023'], axis=1, errors='ignore')
        mask = df_fact['Country Name'] == 'World'
        df_fact = df_fact[~mask]
        mask = df_fact['Country Name'] == "High income"
        df_fact = df_fact[~mask]
        mask = df_fact['Country Name'] == 'Low income'
        df_fact = df_fact[~mask]
        mask = df_fact['Country Name'] == 'Lower middle income'
        df_fact = df_fact[~mask]
        mask = df_fact['Country Name'] == 'Upper middle income'
        df_fact = df_fact[~mask]

        header_list=['Country Name', 'Country Code',fact+" "+ 'Indicator Name', fact+" "+ 'Indicator Code', fact+" "+ '1960', fact+" "+ '1961', fact+" "+ '1962', fact+" "+ '1963', fact+" "+ '1964', fact+" "+ '1965', fact+" "+ '1966', fact+" "+ '1967', fact+" "+ '1968', fact+" "+ '1969', fact+" "+ '1970', fact+" "+ '1971', fact+" "+ '1972', fact+" "+ '1973', fact+" "+ '1974', fact+" "+ '1975', fact+" "+ '1976', fact+" "+ '1977', fact+" "+ '1978', fact+" "+ '1979', fact+" "+ '1980', fact+" "+ '1981', fact+" "+ '1982', fact+" "+ '1983', fact+" "+ '1984', fact+" "+ '1985', fact+" "+ '1986', fact+" "+ '1987', fact+" "+ '1988', fact+" "+ '1989', fact+" "+ '1990', fact+" "+ '1991', fact+" "+ '1992', fact+" "+ '1993', fact+" "+ '1994', fact+" "+ '1995', fact+" "+ '1996', fact+" "+ '1997', fact+" "+ '1998', fact+" "+ '1999', fact+" "+ '2000', fact+" "+ '2001', fact+" "+ '2002', fact+" "+ '2003', fact+" "+ '2004', fact+" "+ '2005', fact+" "+ '2006', fact+" "+ '2007', fact+" "+ '2008', fact+" "+ '2009', fact+" "+ '2010', fact+" "+ '2011', fact+" "+ '2012', fact+" "+ '2013', fact+" "+ '2014', fact+" "+ '2015', fact+" "+ '2016', fact+" "+ '2017', fact+" "+ '2018', fact+" "+ '2019', fact+" "+ '2020', fact+" "+ '2021', fact+" "+ '2022']
        
        df=df_fact.set_axis(header_list,axis=1)
        df_final = pd.merge(df_final, df, on=l)
    
    dim_list = [ element+' '+year_dropdown_pg8 if isinstance(element, str) else element for element in factor_pg8]
    
    fig = px.parallel_coordinates(df_final,color='Income Group',
                            dimensions=dim_list,
                            color_continuous_scale=px.colors.diverging.Tealrose,
                            color_continuous_midpoint=2)
    return fig

layout = html.Div([
    html.H1('This is our page 8'),
    html.Br(),
    dcc.Dropdown(
        options=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],
        value="2018",
        id="year_dropdown_pg8",
        style={"width": "100%"}
    ),
    dcc.Dropdown(
        options=[
            {'label': 'Population', 'value': 'pop_tot_updated'},
            {'label': 'Literacy Rate', 'value': 'literacy_rate_updated'},
            {'label': 'GDP', 'value': 'gdp_current_updated'},
            {'label': 'GDP per Capita', 'value': 'gdp_per_capita_updated'}
        ],
        value=['literacy_rate_updated','pop_tot_updated','gdp_current_updated'],
        id="factor_pg8",
        multi=True,
        style={"width": "100%"}
    ),
    dcc.Graph(id="parallel_coordinate")
])