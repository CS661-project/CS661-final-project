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
import time

dash.register_page(__name__,order=5)

external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css', '/assets/page4.css']

count_list= ['No', 'Aruba', 'Afghanistan', 'Angola', 'Albania', 'Andorra', 'United Arab Emirates', 'Argentina', 'Armenia', 'American Samoa', 'Antigua and Barbuda', 'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas, The', 'Bosnia and Herzegovina', 'Belarus', 'Belize', 'Bermuda', 'Bolivia', 'Brazil', 'Barbados', 'Brunei Darussalam', 'Bhutan', 'Botswana', 'Central African Republic', 'Canada', 'Switzerland', 'Channel Islands', 'Chile', 'China', "Cote d'Ivoire", 'Cameroon', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Curacao', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt, Arab Rep.', 'Eritrea', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji', 'France', 'Faroe Islands', 'Micronesia, Fed. Sts.', 'Gabon', 'United Kingdom', 'Georgia', 'Ghana', 'Gibraltar', 'Guinea', 'Gambia, The', 'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland', 'Guatemala', 'Guam', 'Guyana', 'Hong Kong SAR, China', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Isle of Man', 'India', 'Ireland', 'Iran, Islamic Rep.', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya', 'Kyrgyz Republic', 'Cambodia', 'Kiribati', 'St. Kitts and Nevis', 'Korea, Rep.', 'Kuwait', 'Lao PDR', 'Lebanon', 'Liberia', 'Libya', 'St. Lucia', 'Liechtenstein', 'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao SAR, China', 'St. Martin (French part)', 'Morocco', 'Monaco', 'Moldova', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Northern Mariana Islands', 'Mozambique', 'Mauritania', 'Mauritius', 'Malawi', 'Malaysia', 'Namibia', 'New Caledonia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Pakistan', 'Panama', 'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland', 'Puerto Rico', "Korea, Dem. People's Rep.", 'Portugal', 'Paraguay', 'West Bank and Gaza', 'French Polynesia', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal', 'Singapore', 'Solomon Islands', 'Sierra Leone', 'El Salvador', 'San Marino', 'Somalia', 'Serbia', 'South Sudan', 'Sao Tome and Principe', 'Suriname', 'Slovak Republic', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)', 'Seychelles', 'Syrian Arab Republic', 'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Turkmenistan', 'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkiye', 'Tuvalu', 'Tanzania', 'Uganda', 'Ukraine', 'Uruguay', 'United States', 'Uzbekistan', 'St. Vincent and the Grenadines', 'Venezuela, RB', 'British Virgin Islands', 'Virgin Islands (U.S.)', 'Viet Nam', 'Vanuatu', 'Samoa', 'Kosovo', 'Yemen, Rep.', 'South Africa', 'Zambia', 'Zimbabwe'] 
yr_list=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
                
df_gdp = pd.read_csv('./Data_files/gdp_current_updated.csv')
df_primary = pd.read_csv('./Data_files/percent_pop_in_agri_updated.csv')
df_secondary = pd.read_csv('./Data_files/percent_pop_in_industry_updated.csv')
df_tertiary = pd.read_csv('./Data_files/percent_pop_in_services_updated.csv')
df_primary.set_index("Country Name", inplace = True)
df_secondary.set_index("Country Name", inplace = True)
df_tertiary.set_index("Country Name", inplace = True)
mask = df_gdp['Country Name'] == 'World'
df_gdp=df_gdp[~mask]
df_gdp.set_index("Country Name", inplace = True)

year_manan = "2022"

def generate_sectoral_chart(country_dropdown_pg4,year_dropdown_pg4):
    # time.sleep(2)
    if type(country_dropdown_pg4)== str and type(year_dropdown_pg4) == str:
        gdp_series = df_gdp.loc[country_dropdown_pg4][3:-1]  # Exclude the first two columns (Country Code and Indicator Name) and the last column (2023)
        max_gdp = gdp_series.max()
        # max_gdp=df_gdp[year_dropdown_pg4].max()
        g=df_gdp.loc[country_dropdown_pg4, year_dropdown_pg4]
        p=df_primary.loc[country_dropdown_pg4, year_dropdown_pg4]
        s=df_secondary.loc[country_dropdown_pg4, year_dropdown_pg4]
        t=df_tertiary.loc[country_dropdown_pg4, year_dropdown_pg4]
        fig = go.Figure(data=go.Scatterpolar(
            r=[p,s,t,(g/max_gdp)*100],
            theta=['Primary Sector','Secondary Sector','Tertiary Sector','Normalized GDP'],
            fill='toself'
        ))
    elif len(country_dropdown_pg4)>=1 and type(year_dropdown_pg4) == str:
        # max_gdp=df_gdp[year_dropdown_pg4].max()
        fig=go.Figure()
        max_gdp = max([df_gdp.loc[country][3:-1].max() for country in country_dropdown_pg4])
        for country in country_dropdown_pg4:
            g=df_gdp.loc[country, year_dropdown_pg4]
            p=df_primary.loc[country, year_dropdown_pg4]
            s=df_secondary.loc[country, year_dropdown_pg4]
            t=df_tertiary.loc[country, year_dropdown_pg4]
            fig.add_trace(go.Scatterpolar(
                r=[p,s,t,(g/max_gdp)*100],
                theta=['Primary Sector','Secondary Sector','Tertiary Sector','Normalized GDP'],
                fill='toself',
                name=country
            ))
    else:
        fig = generate_empty_chart()

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 100]
            ),
        ),
        showlegend=False
    )

    return fig

def generate_sectoral_animation(country_dropdown_pg4,year_dropdown_pg4):
    # time.sleep(2)
    fig = generate_empty_chart()
    if(type(country_dropdown_pg4)==str):
        country_dropdown_pg4 = [country_dropdown_pg4]
    if(type(year_dropdown_pg4)==str):
        if(len(country_dropdown_pg4)==0):
            return generate_empty_chart()
        if(type(country_dropdown_pg4)==list):
            country_dropdown_pg4 = str(country_dropdown_pg4[0])
        gdp_series = df_gdp.loc[country_dropdown_pg4][3:-1]  # Exclude the first two columns (Country Code and Indicator Name) and the last column (2023)
        max_gdp = gdp_series.max()
        g=df_gdp.loc[country_dropdown_pg4,year_dropdown_pg4]
        p=df_primary.loc[country_dropdown_pg4, year_dropdown_pg4]
        s=df_secondary.loc[country_dropdown_pg4, year_dropdown_pg4]
        t=df_tertiary.loc[country_dropdown_pg4, year_dropdown_pg4]
        fig = go.Figure(data=go.Scatterpolar(
            r=[p,s,t,(g/max_gdp)*100],
            theta=['Primary Sector','Secondary Sector','Tertiary Sector','Normalized GDP'],
            fill='toself'
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                visible=True,
                range=[0, 100]
                ),
            ),
            showlegend=False
        )
    return fig

@callback(
        Output("sectoral_chart","figure"),
        Input("mode_dropdown_pg4","value"),
        Input("country_dropdown_pg4","value"),
        Input("year_dropdown_pg4","value"),
)
def update_layout(mode_dropdown_pg4,country_dropdown_pg4,year_dropdown_pg4):
    
    if mode_dropdown_pg4 == 'Countries':
        return generate_sectoral_chart(country_dropdown_pg4,year_dropdown_pg4)
    elif mode_dropdown_pg4 == 'Animation':                                                                       #animation left ------> not able to do it, may add slider instead
        # print("Animation")
        return generate_sectoral_animation(country_dropdown_pg4,year_dropdown_pg4)
    else:
        return generate_empty_chart()


@callback(
        Output("year_dropdown_pg4", "value"),
        Input("year_dropdown_pg4", "value"),
        Input("interval-component", "n_intervals"),
        Input("mode_dropdown_pg4", "value"),
        Input("country_dropdown_pg4", "value"),
        Prevent_initial_update = True,
)
def recall(year_dropdown_pg4, n_intervals, mode_dropdown_pg4, country_dropdown_pg4):
    # print(type(year_dropdow_pg4))
    if mode_dropdown_pg4=='Animation':
        # print(type(country_dropdown_pg4))
        if(type(country_dropdown_pg4)!=str and len(country_dropdown_pg4)==0):
            return '1991'
        if(type(year_dropdown_pg4)==str):
            if(int(year_dropdown_pg4)>=2022 or int(year_dropdown_pg4)<1991):
                return '1991'
            return str(int(year_dropdown_pg4)+1)
    return (year_dropdown_pg4)

def generate_empty_chart():
    max_gdp=1
    g=0
    p=0
    s=0
    t=0
    fig = go.Figure(data=go.Scatterpolar(
        r=[p,s,t,(g/max_gdp)*100],
        theta=['Primary Sector','Secondary Sector','Tertiary Sector','Normalized GDP'],
        fill='toself'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 100]
            ),
        ),
        showlegend=False
    )

    return fig

layout = html.Div([
    # Text container
    html.Div(className="text-container",
             children=[
                 html.H1('This is page 4'),
             ]
             ),
    # Dropdown container
    html.Div(className="dropdown-container",
             children=[
                 dcc.Dropdown(
                     options=['Countries', 'Animation'],
                     value="Countries",
                     id="mode_dropdown_pg4",
                     style={"width": "40%"}
                 ),
                 dcc.Dropdown(
                     options=count_list,
                     value="India",
                     id="country_dropdown_pg4",
                     multi=True,
                     style={"width": "40%"}
                 ),
                 dcc.Dropdown(
                     options=yr_list,
                     value="2018",
                     id="year_dropdown_pg4",
                     style={"width": "40%"}
                 ),
             ]
             ),
    # Plot container
    html.Div(className="plot-container",
             children=[
                 dcc.Graph(id="sectoral_chart"),
                 dcc.Interval(
                     id='interval-component',
                     interval=1 * 1500,  # in milliseconds
                     n_intervals=0
                 ),
             ]
             ),
])
