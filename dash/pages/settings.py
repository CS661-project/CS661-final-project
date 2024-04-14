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
global_options=[{'label':'Population','value':'pop_tot_updated'},
         {'label':'Population Growth','value':'pop_growth_updated'},
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
    print(extrapolate_settings)
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

    for iter in range(2):
        if(iter==1):
            if flag==1:
                df= pd.read_csv('./Data_files/'+filename[:-4]+"_updated.csv") 
            else:
                df= pd.read_csv('./Data_files/uploaded_'+filename[:-4]+"_updated.csv") 
        for index,row in df.iterrows():
            b_yr=1960
            f_yr=-1
            count=0
            delta=0
            delta_f=0
            for i in range(1960,2023):
                if(count==0 and pd.isna(row[str(i)])):
                    delta=0
                    f_yr=-1
                    continue
                elif(pd.isna(row[str(i)])!=True and count!=0):
                    delta=0
                    f_yr=-1
                    b_yr=i

                elif(pd.isna(row[str(i)])!=True and count==0):
                    delta=0
                    f_yr=-1
                    b_yr=i
                    count=1
                elif(pd.isna(row[str(i)]) and count!=0):
                    if(f_yr!=-1):
                        df.at[index,str(i)]=row[str(b_yr)]+delta*(i-b_yr)
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
                        else:
                            if(iter==1):
                                print("in final case")
                                for k in range(int(extra_const)):
                                    delta_f=delta_f+(row[str(b_yr-k)]-row[str(b_yr-k-1)])/row[str(b_yr-k-1)]
                                delta_f=delta_f/int(extra_const)
                                for j in range(b_yr+1,2023):
                                    df.at[index,str(j)]=row[str(b_yr)]*(pow((1+delta_f),(j-b_yr)))
                                    print(index,row[str(b_yr)]*(pow((1+delta_f),(j-b_yr))))
                                break
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
    directory_path = '.\Data_files'
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
    directory_path = '.\Data_files'
    p1="electricity"
    p2="export_per"
    p3="imports"
    p4="individuals"
    d_list=["electricity","export_per"]
    for filename in os.listdir(directory_path):
        if filename.startswith(p1):
            continue
        if filename.startswith(p2):
            continue
        if filename.startswith(p3):
            continue
        if filename.startswith(p4):
            continue
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

