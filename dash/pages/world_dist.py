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


dash.register_page(__name__,order=7)

count_list= ['No', 'Aruba', 'Afghanistan', 'Angola', 'Albania', 'Andorra', 'United Arab Emirates', 'Argentina', 'Armenia', 'American Samoa', 'Antigua and Barbuda', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas, The', 'Bosnia and Herzegovina', 'Belarus', 'Belize', 'Bermuda', 'Bolivia', 'Brazil', 'Barbados', 'Brunei Darussalam', 'Bhutan', 'Botswana', 'Central African Republic', 'Canada', 'Switzerland', 'Channel Islands', 'Chile', 'China', "Cote d'Ivoire", 'Cameroon', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Curacao', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt, Arab Rep.', 'Eritrea', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'France', 'Faroe Islands', 'Micronesia, Fed. Sts.', 'Gabon', 'United Kingdom', 'Georgia', 'Ghana', 'Gibraltar', 'Guinea', 'Gambia, The', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland', 'Guatemala', 'Guam', 'Guyana', 'Hong Kong SAR, China', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'Ireland', 'Iran, Islamic Rep.', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyz Republic', 'Cambodia', 'Kiribati', 'St. Kitts and Nevis', 'Korea, Rep.', 'Kuwait', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'St. Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao SAR, China', 'St. Martin (French part)', 'Morocco', 'Monaco', 'Moldova', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Mauritius', 'Malawi', 'Malaysia', 'Namibia', 'New Caledonia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico', "Korea, Dem. People's Rep.", 'Portugal', 'Paraguay', 'West Bank and Gaza', 'French Polynesia', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovak Republic', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles', 'Syrian Arab Republic', 'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkiye', 'Tuvalu', 'Tanzania', 'Uganda', 'Ukraine', 'Uruguay', 'United States', 'Uzbekistan', 'St. Vincent and the Grenadines', 'Venezuela, RB', 'British Virgin Islands', 'Virgin Islands (U.S.)', 'Viet Nam', 'Vanuatu', 'Samoa', 'Kosovo', 'Yemen, Rep.', 'South Africa', 'Zambia', 'Zimbabwe'] 

@callback(
        Output("world_dist_map", "figure"),
        [Input("para_dropdown","value")]
)
def generate_world_dist(para_dropdown):
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
    return fig

@callback(
        Output("country_dropdown","value"),
        Input("world_dist_map","clickData")
)
def change_country_dropdown(clickData):
    if clickData is None:
        return "No"
    return clickData['points'][0]['text']

@callback(
        Output("count_specific","children"),
        Input("country_dropdown","value"),
)
def generate_country_specific(country_dropdown):
    if country_dropdown is None:
        return html.Br()
    if country_dropdown=="No":
        return html.Br()
    # print(clickData['points'][0]['text'])
    # country=clickData['points'][0]['text']
    country=country_dropdown
    
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
    subfig.layout.yaxis1.title="GDP per capita"
    subfig.update_layout(
        title_text="Name: "+country,
    )
    return dcc.Graph(id="country_map",figure=subfig)


layout = html.Div([
    html.H1('This is our World distribution page'),
    html.Br(),
    dcc.Dropdown(
                options=['No', 'gdp_per_capita'],
                value="No",
                id="para_dropdown",
                style={"width": "40%"}
            ),
    dcc.Graph(id="world_dist_map"),
    dcc.Dropdown(
                options=count_list,
                value="No",
                id="country_dropdown",
                style={"width": "40%"}
            ),
    html.Div(id="count_specific")
])