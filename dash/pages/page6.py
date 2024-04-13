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

data = {
    "name": "Income Distribution (216)",
                        "children": [{
                            "name": "Low income (26)",
                            "children": [{
                                "name": "Afghanistan",
                                "children": []
                            }, {
                                "name": "Burundi",
                                "children": []
                            }, {
                                "name": "Burkina Faso",
                                "children": []
                            }, {
                                "name": "Central African Republic",
                                "children": []
                            }, {
                                "name": "Congo, Dem. Rep.",
                                "children": []
                            }, {
                                "name": "Eritrea",
                                "children": []
                            }, {
                                "name": "Ethiopia",
                                "children": []
                            }, {
                                "name": "Gambia, The",
                                "children": []
                            }, {
                                "name": "Guinea-Bissau",
                                "children": []
                            }, {
                                "name": "Liberia",
                                "children": []
                            }, {
                                "name": "Madagascar",
                                "children": []
                            }, {
                                "name": "Mali",
                                "children": []
                            }, {
                                "name": "Mozambique",
                                "children": []
                            }, {
                                "name": "Malawi",
                                "children": []
                            }, {
                                "name": "Niger",
                                "children": []
                            }, {
                                "name": "Korea, Dem. People's Rep.",
                                "children": []
                            }, {
                                "name": "Rwanda",
                                "children": []
                            }, {
                                "name": "Sudan",
                                "children": []
                            }, {
                                "name": "Sierra Leone",
                                "children": []
                            }, {
                                "name": "Somalia",
                                "children": []
                            }, {
                                "name": "South Sudan",
                                "children": []
                            }, {
                                "name": "Syrian Arab Republic",
                                "children": []
                            }, {
                                "name": "Chad",
                                "children": []
                            }, {
                                "name": "Togo",
                                "children": []
                            }, {
                                "name": "Uganda",
                                "children": []
                            }, {
                                "name": "Yemen, Rep.",
                                "children": []
                            }],
                            "child": "true"
                        }, {
                            "name": "Lower middle income (54)",
                            "children": [{
                                "name": "Angola",
                                "children": []
                            }, {
                                "name": "Benin",
                                "children": []
                            }, {
                                "name": "Bangladesh",
                                "children": []
                            }, {
                                "name": "Bolivia",
                                "children": []
                            }, {
                                "name": "Bhutan",
                                "children": []
                            }, {
                                "name": "Côte d'Ivoire",
                                "children": []
                            }, {
                                "name": "Cameroon",
                                "children": []
                            }, {
                                "name": "Congo, Rep.",
                                "children": []
                            }, {
                                "name": "Comoros",
                                "children": []
                            }, {
                                "name": "Cabo Verde",
                                "children": []
                            }, {
                                "name": "Djibouti",
                                "children": []
                            }, {
                                "name": "Algeria",
                                "children": []
                            }, {
                                "name": "Egypt, Arab Rep.",
                                "children": []
                            }, {
                                "name": "Micronesia, Fed. Sts.",
                                "children": []
                            }, {
                                "name": "Ghana",
                                "children": []
                            }, {
                                "name": "Guinea",
                                "children": []
                            }, {
                                "name": "Honduras",
                                "children": []
                            }, {
                                "name": "Haiti",
                                "children": []
                            }, {
                                "name": "India",
                                "children": []
                            }, {
                                "name": "Iran, Islamic rep.",
                                "children": []
                            }, {
                                "name": "Jordan",
                                "children": []
                            }, {
                                "name": "Kenya",
                                "children": []
                            }, {
                                "name": "Kyrgyz Republic",
                                "children": []
                            }, {
                                "name": "Cambodia",
                                "children": []
                            }, {
                                "name": "Kiribati",
                                "children": []
                            }, {
                                "name": "Lao PDR",
                                "children": []
                            }, {
                                "name": "Lebanon",
                                "children": []
                            }, {
                                "name": "Sri Lanka",
                                "children": []
                            }, {
                                "name": "Lesotho",
                                "children": []
                            }, {
                                "name": "Morocco",
                                "children": []
                            }, {
                                "name": "Myanmar",
                                "children": []
                            }, {
                                "name": "Mongolia",
                                "children": []
                            }, {
                                "name": "Mauritania",
                                "children": []
                            }, {
                                "name": "Nigeria",
                                "children": []
                            }, {
                                "name": "Nicaragua",
                                "children": []
                            }, {
                                "name": "Nepal",
                                "children": []
                            }, {
                                "name": "Pakistan",
                                "children": []
                            }, {
                                "name": "Philippines",
                                "children": []
                            }, {
                                "name": "Papua New Guinea",
                                "children": []
                            }, {
                                "name": "Senegal",
                                "children": []
                            }, {
                                "name": "Solomon Islands",
                                "children": []
                            }, {
                                "name": "São Tomé and Principe",
                                "children": []
                            }, {
                                "name": "Eswatini",
                                "children": []
                            }, {
                                "name": "Tajikistan",
                                "children": []
                            }, {
                                "name": "Timor-Leste",
                                "children": []
                            }, {
                                "name": "Tunisia",
                                "children": []
                            }, {
                                "name": "Tanzania",
                                "children": []
                            }, {
                                "name": "Ukraine",
                                "children": []
                            }, {
                                "name": "Uzbekistan",
                                "children": []
                            }, {
                                "name": "Viet Nam",
                                "children": []
                            }, {
                                "name": "Vanuatu",
                                "children": []
                            }, {
                                "name": "Samoa",
                                "children": []
                            }, {
                                "name": "Zambia",
                                "children": []
                            }, {
                                "name": "Zimbabwe",
                                "children": []
                            }],
                            "child": "true"
                        }, {
                            "name": "Upper middle income (54)",
                            "children": [{
                                "name": "Albania",
                                "children": []
                            }, {
                                "name": "Argentina",
                                "children": []
                            }, {
                                "name": "Armenia",
                                "children": []
                            }, {
                                "name": "Azerbaijan",
                                "children": []
                            }, {
                                "name": "Bulgaria",
                                "children": []
                            }, {
                                "name": "Bosnia and Herzegovina",
                                "children": []
                            }, {
                                "name": "Belarus",
                                "children": []
                            }, {
                                "name": "Belize",
                                "children": []
                            }, {
                                "name": "Brazil",
                                "children": []
                            }, {
                                "name": "Botswana",
                                "children": []
                            }, {
                                "name": "China",
                                "children": []
                            }, {
                                "name": "Colombia",
                                "children": []
                            }, {
                                "name": "Costa Rica",
                                "children": []
                            }, {
                                "name": "Cuba",
                                "children": []
                            }, {
                                "name": "Dominica",
                                "children": []
                            }, {
                                "name": "Dominican Republic",
                                "children": []
                            }, {
                                "name": "Ecuador",
                                "children": []
                            }, {
                                "name": "Fiji",
                                "children": []
                            }, {
                                "name": "Gabon",
                                "children": []
                            }, {
                                "name": "Georgia",
                                "children": []
                            }, {
                                "name": "Equatorial Guinea",
                                "children": []
                            }, {
                                "name": "Grenada",
                                "children": []
                            }, {
                                "name": "Guatemala",
                                "children": []
                            }, {
                                "name": "Indonesia",
                                "children": []
                            }, {
                                "name": "Iraq",
                                "children": []
                            }, {
                                "name": "Jamaica",
                                "children": []
                            }, {
                                "name": "Kazakhstan",
                                "children": []
                            }, {
                                "name": "Libya",
                                "children": []
                            }, {
                                "name": "St. Lucia",
                                "children": []
                            }, {
                                "name": "Moldova",
                                "children": []
                            }, {
                                "name": "Maldives",
                                "children": []
                            }, {
                                "name": "Mexico",
                                "children": []
                            }, {
                                "name": "Marshall Islands",
                                "children": []
                            }, {
                                "name": "North Macedonia",
                                "children": []
                            }, {
                                "name": "Montenegro",
                                "children": []
                            }, {
                                "name": "Mauritius",
                                "children": []
                            }, {
                                "name": "Malaysia",
                                "children": []
                            }, {
                                "name": "Namibia",
                                "children": []
                            }, {
                                "name": "Peru",
                                "children": []
                            }, {
                                "name": "Palau",
                                "children": []
                            }, {
                                "name": "Paraguay",
                                "children": []
                            }, {
                                "name": "West bank and Gaza",
                                "children": []
                            }, {
                                "name": "Russian Federation",
                                "children": []
                            }, {
                                "name": "El Salvador",
                                "children": []
                            }, {
                                "name": "Serbia",
                                "children": []
                            }, {
                                "name": "Suriname",
                                "children": []
                            }, {
                                "name": "Thailand",
                                "children": []
                            }, {
                                "name": "Turkmenistan",
                                "children": []
                            }, {
                                "name": "Tonga",
                                "children": []
                            }, {
                                "name": "Türkiye",
                                "children": []
                            }, {
                                "name": "Tuvalu",
                                "children": []
                            }, {
                                "name": "St. Vincent and the Grenadines",
                                "children": []
                            }, {
                                "name": "Kosovo",
                                "children": []
                            }, {
                                "name": "South Africa",
                                "children": []
                            }],
                            "child": "true" 
                        }, {
                            "name": "High income (82)",
                            "children": [{
                                "name": "Aruba",
                                "children": []
                            }, {
                                "name": "Andorra",
                                "children": []
                            }, {
                                "name": "United Arab Emirates",
                                "children": []
                            }, {
                                "name": "American Samoa",
                                "children": []
                            }, {
                                "name": "Antigua and Barbuda",
                                "children": []
                            }, {
                                "name": "Australia",
                                "children": []
                            }, {
                                "name": "Austria",
                                "children": []
                            }, {
                                "name": "Belgium",
                                "children": []
                            }, {
                                "name": "Bahrain",
                                "children": []
                            }, {
                                "name": "Bahamas, The",
                                "children": []
                            }, {
                                "name": "Bermuda",
                                "children": []
                            }, {
                                "name": "Barbados",
                                "children": []
                            }, {
                                "name": "Brunei Darussalam",
                                "children": []
                            }, {
                                "name": "Canada",
                                "children": []
                            }, {
                                "name": "Switzerland",
                                "children": []
                            }, {
                                "name": "Channel Islands",
                                "children": []
                            }, {
                                "name": "Chile",
                                "children": []
                            }, {
                                "name": "Curaçao",
                                "children": []
                            }, {
                                "name": "Cayman Islands",
                                "children": []
                            }, {
                                "name": "Cyprus",
                                "children": []
                            }, {
                                "name": "Czechia",
                                "children": []
                            }, {
                                "name": "Germany",
                                "children": []
                            }, {
                                "name": "Denmark",
                                "children": []
                            }, {
                                "name": "Spain",
                                "children": []
                            }, {
                                "name": "Estonia",
                                "children": []
                            }, {
                                "name": "Finland",
                                "children": []
                            }, {
                                "name": "France",
                                "children": []
                            }, {
                                "name": "Faroe Islands",
                                "children": []
                            }, {
                                "name": "United Kingdom",
                                "children": []
                            }, {
                                "name": "Gibraltar",
                                "children": []
                            }, {
                                "name": "Greece",
                                "children": []
                            }, {
                                "name": "Greenland",
                                "children": []
                            }, {
                                "name": "Guam",
                                "children": []
                            }, {
                                "name": "Guyana",
                                "children": []
                            }, {
                                "name": "Hong Kong SAR, China",
                                "children": []
                            }, {
                                "name": "Croatia",
                                "children": []
                            }, {
                                "name": "Hungary",
                                "children": []
                            }, {
                                "name": "Isle of Man",
                                "children": []
                            }, {
                                "name": "Ireland",
                                "children": []
                            }, {
                                "name": "Iceland",
                                "children": []
                            }, {
                                "name": "Israel",
                                "children": []
                            }, {
                                "name": "Italy",
                                "children": []
                            }, {
                                "name": "Japan",
                                "children": []
                            }, {
                                "name": "St. Kitts and Nevis",
                                "children": []
                            }, {
                                "name": "Korea, Rep.",
                                "children": []
                            }, {
                                "name": "Kuwait",
                                "children": []
                            }, {
                                "name": "Liechtenstein",
                                "children": []
                            }, {
                                "name": "Lithuania",
                                "children": []
                            }, {
                                "name": "Luxembourg",
                                "children": []
                            }, {
                                "name": "Latvia",
                                "children": []
                            }, {
                                "name": "Macao SAR, China",
                                "children": []
                            }, {
                                "name": "St. Martin (French part)",
                                "children": []
                            }, {
                                "name": "Monaco",
                                "children": []
                            }, {
                                "name": "Malta",
                                "children": []
                            }, {
                                "name": "Northern Mariana Islands",
                                "children": []
                            }, {
                                "name": "New Caledonia",
                                "children": []
                            }, {
                                "name": "Netherlands",
                                "children": []
                            }, {
                                "name": "Norway",
                                "children": []
                            }, {
                                "name": "Nauru",
                                "children": []
                            }, {
                                "name": "New Zealand",
                                "children": []
                            }, {
                                "name": "Oman",
                                "children": []
                            }, {
                                "name": "Panama",
                                "children": []
                            }, {
                                "name": "Poland",
                                "children": []
                            }, {
                                "name": "Puerto Rico",
                                "children": []
                            }, {
                                "name": "Portugal",
                                "children": []
                            }, {
                                "name": "French Polynesia",
                                "children": []
                            }, {
                                "name": "Qatar",
                                "children": []
                            }, {
                                "name": "Romania",
                                "children": []
                            }, {
                                "name": "Saudi Arabia",
                                "children": []
                            }, {
                                "name": "Singapore",
                                "children": []
                            }, {
                                "name": "San Marino",
                                "children": []
                            }, {
                                "name": "Slovak Republic",
                                "children": []
                            }, {
                                "name": "Slovenia",
                                "children": []
                            }, {
                                "name": "Sweden",
                                "children": []
                            }, {
                                "name": "Sint Maarten (Dutch part)",
                                "children": []
                            }, {
                                "name": "Seychelles",
                                "children": []
                            }, {
                                "name": "Turks and Caicos Islands",
                                "children": []
                            }, {
                                "name": "Trinidad and Tobago",
                                "children": []
                            }, {
                                "name": "Uruguay",
                                "children": []
                            }, {
                                "name": "United States",
                                "children": []
                            }, {
                                "name": "British Virgin Islands",
                                "children": []
                            }, {
                                "name": "Virgin Islands (U.S.)",
                                "children": []
                            }],
                            "child": "true"
                        }]}

opts = {
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove",
    },
    "series": [
        {
            "type": "tree",
            "data": [data],
            "top": "1%",
            "left": "10%",
            "bottom": "1%",
            "right": "20%",
            "symbolSize": 7,
            "label": {
                "position": "bottom",
                "verticalAlign": "middle",
                "align": "right",
                "fontSize": 10,
                "color": "black",
            },
            "leaves": {
                "label": {
                    "position": "right",
                    "verticalAlign": "middle",
                    "align": "left",
                }
            },
            # "emphasis": {
            #     "focus": 'descendant'
            # },
            "expandAndCollapse": True,
            "animationDuration": 550,
            "animationDurationUpdate": 750,
        },
        
    ],
}

layout = html.Div([
    html.H1('This is page 6'),
    html.Br(),
    # html.Div([
    #     dcc.Dropdown(
    #         options=['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],
    #         value="2018",
    #         id="year_dropdown_pg1",
    #         style={"width": "60%"}
    #     ),
    #     dcc.Dropdown(
    #         options=[
    #             {'label':'Population','value':'pop_tot_updated'},
    #             {'label':'Population Growth','value':'pop_growth_updated'},
    #         ],
    #         value="pop_tot_updated",
    #         id="factor_pg1",
    #         style={"width": "60%"}
    #     ),
    # ], style={"display": "flex", "justify-content": "space-evenly", "margin-bottom": "10px", "padding-left": "100px"}),
    html.Div([
    dash_echarts.DashECharts(
        option = opts,
        id='echarts',
        style={
            "width": '100vw',
            "height": '100vh',
        }
    ),
    # dcc.Graph(id="line_graph")

])
], className="page1_style")



# # df_w_fact=pd.read_csv('./Data_files/pop_tot_updated.csv') #global, will implement

# df_w_gdp = pd.read_csv('./Data_files/gdp_current_updated.csv')

# df_w_gdp_t=df_w_gdp.transpose()
# new_header = df_w_gdp_t.iloc[0] 
# df_w_gdp_t = df_w_gdp_t[4:]
# df_w_gdp_t.columns = new_header
# df_w_gdp_t.index.name = 'year'
# df_w_gdp_t.to_csv('update.csv')
# df_w_gdp_t = pd.read_csv('update.csv')

# fig = px.line(df_w_gdp_t, x="year", y="World")

# fig.layout.xaxis.title="Year"
# fig.layout.yaxis.title="GDP"
# # subfig.update_layout(
# #     title_text="Name: "+country,
# # )

# @callback(
#         Output("top10_gdp","figure"),
#         Input("year_dropdown_pg1","value"),
# )
# def generate_top_10_gdp(year_dropdown_pg1):
#     sorted_df_w_gdp = df_w_gdp.sort_values(by=year_dropdown_pg1, ascending=False)
#     sorted_df_w_gdp_top_10_rows = sorted_df_w_gdp.head(11)
#     sorted_df_w_gdp_top_10_rows=sorted_df_w_gdp_top_10_rows[1:]
#     fig = px.bar(sorted_df_w_gdp_top_10_rows,
#                   y=year_dropdown_pg1, x="Country Name"
#                   )
#     fig.layout.xaxis.title="Countries"
#     fig.layout.yaxis.title="GDP"
#     return fig

# @callback(
#         Output("factor_vs_year","figure"),
#         Input("factor_pg1","value"),
# )
# def generate_w_factor(factor_pg1):
#     df_w_fact=pd.read_csv('./Data_files/'+factor_pg1+'.csv')
#     df_w_fact_t=df_w_fact.transpose()
#     new_header = df_w_fact_t.iloc[0] 
#     df_w_fact_t = df_w_fact_t[4:]
#     df_w_fact_t.columns = new_header
#     df_w_fact_t.index.name = 'year'
#     df_w_fact_t.to_csv('update.csv')
#     df_w_fact_t = pd.read_csv('update.csv')

#     fig = px.line(df_w_fact_t, x="year", y="World")

#     fig.layout.xaxis.title="Year"
#     fig.layout.yaxis.title=factor_pg1
#     return fig

# @callback(
#         Output("top10_factor","figure"),
#         Input("year_dropdown_pg1","value"),
#         Input("factor_pg1","value"),
# )
# def generate_top_10_factor(year_dropdown_pg1,factor_pg1):
#     df_w_fact=pd.read_csv('./Data_files/'+factor_pg1+'.csv')
#     sorted_df_w_fact = df_w_fact.sort_values(by=year_dropdown_pg1, ascending=False)
#     sorted_df_w_fact_top_10_rows = sorted_df_w_fact.head(11)
#     sorted_df_w_fact_top_10_rows=sorted_df_w_fact_top_10_rows[1:]
#     fig = px.bar(sorted_df_w_fact_top_10_rows,
#                   y="Country Name", x=year_dropdown_pg1
#                   )
#     fig.layout.xaxis.title=factor_pg1
#     fig.layout.yaxis.title="Countries"
#     return fig


#  html.Div([
#         html.Div([
#             dcc.Graph(id="world_gdp", figure=fig, style={"height": "300px"}),
#             dcc.Graph(id="top10_gdp", style={"height": "300px"})
#         ], style={"flex": "1"}),
#         html.Div([
#             dcc.Graph(id="factor_vs_year", style={"height": "300px"}),
#             dcc.Graph(id="top10_factor", style={"height": "300px"})
#         ], style={"flex": "1"})
#     ], className="grid-container")