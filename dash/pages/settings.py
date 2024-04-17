import plotly.express as px
import pandas as pd
import dash
from dash import Dash, dcc, Input, Output, html, callback, ctx,State
import json
import dash_echarts
from dash.exceptions import PreventUpdate
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import base64
import datetime
import io
import os


dash.register_page(__name__,order=10)


global global_k
global_k='Filter'

global extrapolate_const
extrapolate_const="5"

global global_options
global_options=[
    {"label": "Access To Electricity", "value": "access_to_electricity_updated"},
    {"label": "Adjusted Net Income Per Capita", "value": "adjusted_net_income_per_capita_updated"},
    {"label": "Age Dependency Ratio", "value": "age_dependency_ratio_updated"},
    {"label": "Agriculture Percent Gdp", "value": "agriculture_percent_gdp_updated"},
    {"label": "Current Health Expenditure", "value": "current_health_expenditure_updated"},
    {"label": "Education Expend Percent Public Expend", "value": "education_expend_percent_public_expend_updated"},
    {"label": "Electricity Prod Renewable", "value": "electricity_prod_renewable_updated"},
    {"label": "Expense Percent Gdp", "value": "expense_percent_gdp_updated"},
    {"label": "Export Annual Growth", "value": "export_annual_growth_updated"},
    {"label": "Export Percent Of Gdp", "value": "export_percent_of_gdp_updated"},
    {"label": "Female Male Labor Ratio", "value": "female_male_labor_ratio_updated"},
    {"label": "Gdp Current", "value": "gdp_current_updated"},
    {"label": "Gdp Per Capita", "value": "gdp_per_capita_updated"},
    {"label": "Gdp Per Capita percent Growth", "value": "gdp_per_capita_%_growth_updated"},
    {"label": "Imports", "value": "imports_updated"},
    {"label": "Individuals Using The Internet", "value": "individuals_using_the_internet_updated"},
    {"label": "Life Expectancy", "value": "life_expectancy_updated"},
    {"label": "Literacy Rate", "value": "literacy_rate_updated"},
    {"label": "Manufacturing Percent Gdp", "value": "manufacturing_percent_gdp_updated"},
    {"label": "Military Expend", "value": "military_expend_updated"},
    {"label": "Percent Population In Agri", "value": "percent_pop_in_agri_updated"},
    {"label": "Percent Population In Industry", "value": "percent_pop_in_industry_updated"},
    {"label": "Percent Population In Services", "value": "percent_pop_in_services_updated"},
    {"label": "Population Growth", "value": "pop_growth_updated"},
    {"label": "Population Total", "value": "pop_tot_updated"},
    {"label": "R&D Expend Percent Gdp", "value": "r&d_expend_percent_gdp_updated"},
    {"label": "Services Percent Gdp", "value": "services_percent_gdp_updated"}
]

@callback(
        Output("settings_store","data"),
        Input("settings_dropdown","value"),
)
def generate_settings_store(settings_dropdown):
    # print('i m in: ',settings_dropdown)
    global global_k
    global_k=settings_dropdown
    return settings_dropdown

@callback(
        Output("settings_store1","data"),
        Input("extrapolate_settings","value"),
)
def generate_extrapolate_store(extrapolate_settings):
    global extrapolate_const
    extrapolate_const=extrapolate_settings
    return extrapolate_settings

def generate_updated_file(df,filename,flag=0,extra_const="5"):
    countries=[
    "Africa Eastern and Southern",
    "Africa Western and Central",
    "Arab World",
    "Central Europe and the Baltics",
    "Caribbean small states",
    "East Asia & Pacific (excluding high income)",
    "Early-demographic dividend",
    "East Asia & Pacific",
    "Europe & Central Asia (excluding high income)",
    "Europe & Central Asia",
    "Euro area",
    "European Union",
    "Fragile and conflict affected situations",
    "High income",
    "Heavily indebted poor countries (HIPC)",
    "IBRD only",
    "IDA & IBRD total",
    "IDA total",
    "IDA blend",
    "IDA only",
    "Latin America & Caribbean (excluding high income)",
    "Latin America & Caribbean",
    "Least developed countries: UN classification",
    "Low income",
    "Lower middle income",
    "Low & middle income",
    "Late-demographic dividend",
    "Middle East & North Africa",
    "Middle income",
    "Middle East & North Africa (excluding high income)",
    "North America",
    "OECD members",
    "Other small states",
    "Pre-demographic dividend",
    "Pacific island small states",
    "Post-demographic dividend",
    "South Asia",
    "Sub-Saharan Africa (excluding high income)",
    "Sub-Saharan Africa",
    "Small states",
    "East Asia & Pacific (IDA & IBRD)",
    "Europe & Central Asia (IDA & IBRD)",
    "Latin America & Caribbean (IDA & IBRD)",
    "Middle East & North Africa (IDA & IBRD)",
    "South Asia (IDA & IBRD)",
    "Sub-Saharan Africa (IDA & IBRD)",
    "Upper middle income",
    # "World",
    "Sub-Saharan Africa (IDA & IBRD countries)",
    "East Asia & Pacific (IDA & IBRD countries)",
    "Europe & Central Asia (IDA & IBRD countries)",
    "Latin America & the Caribbean (IDA & IBRD countries)",
    "Middle East & North Africa (IDA & IBRD countries)",
    "Not classified",
    ]

    for row in df.iterrows():
        if row[1]['Country Name'] in countries:
            df=df.drop(row[0])
    max_value_lim=0
    min_value_lim=0
    for iter in range(2):
        if(iter==1):
            if flag==1:
                df= pd.read_csv('./Data_files/'+filename[:-4]+"_updated.csv") 
            else:
                df= pd.read_csv('./Data_files/uploaded_'+filename[:-4]+"_updated.csv")
        for index,row in df.iterrows():
            max_value_lim=0
            min_value_lim=0
            # print(df.at[index,'2020'])
            max_delta_lim=5
            min_delta_lim=-5
            b_yr=1960
            f_yr=-1
            count=0
            delta=0
            delta_f=0
            # if(iter==0):
            for j in range(1960,2023):
                if(pd.isna(row[str(j)])==True):
                    continue
                max_value_lim=max(max_value_lim,float(row[str(j)]))
                min_value_lim=min(min_value_lim,float(row[str(j)]))
                # if row['Country Name']=='Eritrea':
                #     print('in : ',max_value_lim, min_value_lim)
            for i in range(1960,2023):
                # print(row[str(i)],'\n')
                #no value read till now
                if(count==0 and pd.isna(row[str(i)])):
                    delta=0
                    f_yr=-1
                    # print("in1")
                    continue
                #value read but not first
                elif(pd.isna(row[str(i)])!=True and count!=0):
                    delta=0
                    f_yr=-1
                    b_yr=i
                    # print("in2")

                # first value read
                elif(pd.isna(row[str(i)])!=True and count==0):
                    delta=0
                    f_yr=-1
                    b_yr=i
                    count=1
                    # print(index,i,"in3")
                elif(pd.isna(row[str(i)]) and count!=0):
                    # print(index,i,"in4")
                    if(f_yr!=-1):
                        df.at[index,str(i)]=row[str(b_yr)]+delta*(i-b_yr)
                        # print(row[str(b_yr)]+delta*(i-b_yr))
                        # print()
                    else:
                        for j in range(b_yr+1,2023):
                            if(pd.isna(row[str(j)])):
                                continue
                            else:
                                f_yr=j
                                delta=(row[str(j)]-row[str(b_yr)])/(j-b_yr)
                                break
                        if(f_yr!=-1):
                            df.at[index,str(i)]=row[str(b_yr)]+delta*(i-b_yr)
                            # print(row[str(b_yr)]+delta*(i-b_yr))
                            # print()
                        else:
                            if(iter==1):
                                # print("in final case")
                                # df.to_csv(filename+"_updated.csv")
                                # df = pd.read_csv(filename+"_updated.csv")
                                div=0
                                for k in range(5):
                                    if b_yr-k-1<1960:
                                        continue
                                    if row[str(b_yr-k-1)]==0:
                                        # print("exc1")
                                        break
                                    if((row[str(b_yr-k)]-row[str(b_yr-k-1)])/row[str(b_yr-k-1)]>max_delta_lim):
                                        delta_f=delta_f+max_delta_lim
                                    elif((row[str(b_yr-k)]-row[str(b_yr-k-1)])/row[str(b_yr-k-1)]<min_delta_lim):
                                        delta_f=delta_f+min_delta_lim
                                    else:
                                        delta_f=delta_f+(row[str(b_yr-k)]-row[str(b_yr-k-1)])/row[str(b_yr-k-1)]
                                    # delta_f=delta_f+(row[str(b_yr-k)]-row[str(b_yr-k-1)])/row[str(b_yr-k-1)]
                                    div=div+1
                                if div==0:
                                    # print("exc2")
                                    delta_f=0
                                else:
                                    delta_f=delta_f/div
                                for j in range(b_yr+1,2023):
                                    if(row[str(b_yr)]*(pow((1+delta_f),(j-b_yr)))<max_value_lim) and (row[str(b_yr)]*(pow((1+delta_f),(j-b_yr)))>min_value_lim):
                                        df.at[index,str(j)]=row[str(b_yr)]*(pow((1+delta_f),(j-b_yr)))
                                    else:
                                        # if row['Country Name']=='Eritrea':
                                        #     print('in : ',max_value_lim, min_value_lim)
                                        df.at[index,str(j)]=max_value_lim if row[str(b_yr)]*(pow((1+delta_f),(j-b_yr)))>max_value_lim else min_value_lim
                                    # print(index,row[str(b_yr)]*(pow((1+delta_f),(j-b_yr))))
                                break

        # print(df)
        if flag==1:
            df.to_csv('./Data_files/'+filename[:-4]+"_updated.csv",index=False)   
        else:
            df.to_csv('./Data_files/uploaded_'+filename[:-4]+"_updated.csv",index=False)

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    print(filename)
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            df.to_csv('./Data_files/uploaded_'+filename,index=False)
            global_options.append({'label':'uploaded_'+filename[:-4],'value':'uploaded_'+filename[:-4]+'_updated'})
            generate_updated_file(df,filename)
   
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

@callback(
        Output('output-data-upload', 'children'),
        Input('upload-data', 'contents'),
        State('upload-data', 'filename'),
        State('upload-data', 'last_modified')
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

@callback(
        Output('del_div', 'children'),
        Input('delete_button', 'n_clicks'),
        prevent_initial_call=True
)
def delete_uploaded_files(n_clicks):
    directory_path = './Data_files'
    prefix = 'uploaded'
    l=["removed files: "]
    l.append('\n')
    for filename in os.listdir(directory_path):
        if filename.startswith(prefix):
            file_path = os.path.join(directory_path, filename)
            os.remove(file_path)
            l.append(filename)
            l.append('\n')
    return l

@callback(
        Output('filter_div', 'children'),
        Input('filter_button', 'n_clicks'),
        prevent_initial_call=True
)
def filter_files(n_clicks):
    directory_path = './Data_files'
    p1="electricity"
    p2="export_per"
    p3="imports"
    p4="individuals"
    d_list=["electricity","export_per"]
    for filename in os.listdir(directory_path):
        # if filename.startswith(p1):
        #     continue
        # if filename.startswith(p2):
        #     continue
        # if filename.startswith(p3):
        #     continue
        # if filename.startswith(p4):
        #     continue
        if filename.endswith("_updated.csv"):
            continue
        print(filename)
        df=pd.read_csv('./Data_files/'+filename)
        generate_updated_file(df,filename,1,extrapolate_const)
    return "DONE!!"


layout = html.Div([
    dcc.Store(id='settings_store'),
    dcc.Store(id='settings_store1'),
    dcc.RadioItems(
        options=[
            {'label': 'Filter', 'value': 'Filter'},
            {'label': 'No Filter', 'value': 'No Filter'}
        ],
        value='Filter',
        id='settings_dropdown',
        inline=True,
        persistence=True
    ),
    html.Br(),
    # dcc.Slider(
    #     id='settings_slider',min=1,max=10,step=1,value=5,
    # ),
    dcc.Dropdown(
            options=[
                "1","2","3","4","5","6","7","8","9","10"
            ],
            value="5",
            id="extrapolate_settings",
            clearable=False,
            style={"width": "40%"}
        ),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
    html.Button('Delete', id='delete_button', n_clicks=0),
    html.Button('Filter', id='filter_button', n_clicks=0),
    html.Div(id="del_div",children="files deleted: "),
    html.Div(id="filter_div",children="files filtered: ")
], className="page1_style")

