import dash
from dash import Dash, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the sidebar content with a collapsible section
sidebar = html.Div([
    html.Div([
        # Hidden input to track sidebar visibility
        dcc.Input(id='sidebar_state', type='hidden', value='closed'),
        # Collapsible button to toggle sidebar visibility
        html.Button('☰', id='toggle_sidebar', className='button_style button_large', style={'margin-right': 'auto', 'background-color': 'skyblue'} ),    
        # Collapsible sidebar content
        dbc.Collapse(
            html.Div([
                html.Button('Homepage', id='home', n_clicks=0, className="button_style" , style={'background-color': 'rgb(173, 216, 230)'}),
                html.Button('World trend', id='pg1', n_clicks=0, className="button_style", style={'background-color': 'rgb(173, 216, 230)'}),
                html.Button('Factor relation', id='pg2', n_clicks=0, className="button_style" , style={'background-color': 'rgb(173, 216, 230)'}),
                html.Button('World Heatmap', id='pg3', n_clicks=0, className="button_style" , style={'background-color': 'rgb(173, 216, 230)'}),
                html.Button('Sectoral Distrib', id='pg4', n_clicks=0, className="button_style" , style={'background-color': 'rgb(173, 216, 230)'}),
                html.Button('Fifth', id='pg5', n_clicks=0, className="button_style" , style={'background-color': 'rgb(173, 216, 230)'}),
                html.Button('Sixth', id='pg6', n_clicks=0, className="button_style" , style={'background-color': 'rgb(173, 216, 230)'}),
                html.Button('Comparison page', id='pg7', n_clicks=0, className="button_style" , style={'background-color': 'rgb(173, 216, 230)'}),
            ]),
            id='collapse_sidebar',
            is_open=False,  # Sidebar initially open
            style={'overflow': 'hidden', 'transition': 'width 0.3s', 'background-color': 'white'}
        ),
    ], style={'width': '150px', 'transition': 'margin-left 0.0s', 'margin-left': '0', 'position': 'fixed', 'top': '0', 'left': '0', 'bottom': '0', 'background-color': 'white'}),
], className="sidebar_style collapse-sidebar")

# Define the initial content as an empty div
initial_content = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='initial-content'),
], className="content_style")

# Define the app layout
app.layout = html.Div([sidebar, initial_content])

# Callback to toggle the sidebar visibility and update sidebar's state
# Combined callback to toggle the sidebar visibility, update sidebar's state, and update sidebar style
@app.callback(
    [Output('collapse_sidebar', 'is_open'),
     Output('sidebar_state', 'value'),
     Output('collapse_sidebar', 'style')],
    [Input('toggle_sidebar', 'n_clicks')],
    [State('sidebar_state', 'value')],
)
def toggle_and_update_sidebar(n, state):
    if n:
        is_open = not state == 'open'
        sidebar_state = 'closed' if state == 'open' else 'open'
        background_color = 'transparent' if sidebar_state == 'open' else 'white'
        return is_open, sidebar_state, {'background-color': background_color}
    else:
        return False, 'closed', {'background-color': 'white'}  # Default style when sidebar is closed

# Callback to update the initial content when buttons are clicked
@app.callback(
    Output('initial-content', 'children'),
    Input('pg1', 'n_clicks'), Input('pg2', 'n_clicks'), Input('pg3', 'n_clicks'),
    Input('pg4', 'n_clicks'), Input('pg5', 'n_clicks'), Input('pg6', 'n_clicks'),
    Input('pg7', 'n_clicks'), Input('home', 'n_clicks')
)
def update_initial_content(n_clicks1, n_clicks2, n_clicks3, n_clicks4,
                           n_clicks5, n_clicks6, n_clicks7, n_clicks_home):
    # Determine which button was clicked
    button_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'home' or not any([n_clicks1, n_clicks2, n_clicks3,
                                       n_clicks4, n_clicks5, n_clicks6, n_clicks7]):
        from pages import home_page
        return home_page.layout
    elif button_id == 'pg1':
        from pages import page1
        return page1.layout
    elif button_id == 'pg2':
        from pages import page2
        return page2.layout
    elif button_id == 'pg3':
        from pages import page3
        return page3.layout
    elif button_id == 'pg4':
        from pages import page4
        return page4.layout
    elif button_id == 'pg5':
        from pages import cross_sect
        return cross_sect.layout
    elif button_id == 'pg6':
        from pages import india_specific
        return india_specific.layout
    elif button_id == 'pg7':
        from pages import page7
        return page7.layout
    else:
        from pages import home_page
        return home_page.layout

if __name__ == '__main__':
    app.run_server(debug=True)



