import dash
from dash import Dash, dcc, Input, Output, html, callback

dash.register_page(__name__, order=1, path='/')

external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css', '/assets/home_page.css']

layout = html.Div([
    html.H1('CS661: BIG DATA VISUAL ANALYTICS', className='Title center-aligned'),
    html.H2('END TERM PROJECT', className='center-aligned'),
    html.H3('DEMOGRAPHIC VISUALIZATION', className='center-aligned'),
    
    html.Div([
        html.H3('Description of Project'),
        html.P(
            'Welcome to our interactive platform designed to explore global economics '
            'through data visualization and analysis. Navigate through our seven-page journey '
            'to delve into the factors shaping the world GDP and gain insights into the global '
            'economic landscape.'
        ),
        html.H4('The page introductions are as follows:'),
        html.Ul([
            html.Li('Global GDP Trends: Explore visuals showcasing global GDP trends and influencing parameters.'),
            html.Li('Country-Specific Correlations: View scatterplots illustrating correlations between GDP and various factors across countries.'),
            html.Li('Countrywise Factor Distribution: Discover the distribution of potential GDP-affecting factors across countries.'),
            html.Li("Sectorial Impact on GDP: Examine the effects of primary, secondary, and tertiary sectors on a country's GDP."),
            html.Li('Income Distribution Analysis: Analyze income distribution among countries, highlighting its impact on various other factors'),
            html.Li('Country-to-Country Comparison: Compare countries based on GDP and related factors using our interactive tool.'),
        ])
    ], className='container center-aligned'),

    html.Div([
        html.H3('Group Members'),
        html.Table([
            html.Tr([
                html.Td('Aastik Guru'), 
                html.Td('Manan Kalavadia'), 
                html.Td('Mayank Saini'), 
                html.Td('Siddhant')
            ]),
            html.Tr([
                html.Td('Abhishek Mishra'), 
                html.Td('Aatman Jain'), 
                html.Td('Yash Gupta'), 
                html.Td('Atharv')
            ])
        ])
    ], className='container center-aligned'),

    html.Div([
        html.H3('Source Code'),
        html.P(html.A('Github Repository', href='https://github.com/CS661-project'))
    ], className='container center-aligned'),

    html.Div([
        html.H3('References'),
        html.P('Reference 1'),
        html.P('Reference 2')
    ], className='container center-aligned')
])
