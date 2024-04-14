import dash
from dash import Dash, dcc, Input, Output, html,callback

dash.register_page(__name__,order=1,path='/')

layout = html.Div([
    html.H1('Exploring Global Economics: A Visual Analysis', style={'textAlign': 'center'}, className='Title'),
    html.Br(),
    html.H2('About our Project'),
    html.H6(
        'Welcome to our interactive platform designed to explore global economics through data visualization and analysis. Navigate through our seven-page journey to delve into the factors shaping the world GDP and gain insights into the global economic landscape.'
       ),
    html.H4('The page introductions are as follows:'),
    html.H6('Global GDP Trends: Explore visuals showcasing global GDP trends and influencing parameters.'),
    html.H6('Country-Specific Correlations: View scatterplots illustrating correlations between GDP and various factors across countries.'),
    html.H6('Countrywise Factor Distribution: Discover the distribution of potential GDP-affecting factors across countries.'),
    html.H6("Sectorial Impact on GDP: Examine the effects of primary, secondary, and tertiary sectors on a country's GDP."),
    html.H6('Income Distribution Analysis: Analyze income distribution among countries, highlighting its impact on various other factors'),
    html.H6('Country-to-Country Comparison: Compare countries based on GDP and related factors using our interactive tool.'),
    html.Br(),
    
    
])
