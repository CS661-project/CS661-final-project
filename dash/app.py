import dash
from dash import Dash, html, dcc, Output, Input

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

# Define the sidebar content
sidebar = html.Div([
    html.Div([
        html.Button('First', id='pg1', n_clicks=0, className="button_style"),
        html.Button('Second', id='pg2', n_clicks=0, className="button_style"),
        html.Button('Third', id='pg3', n_clicks=0, className="button_style"),
        html.Button('Fourth', id='pg4', n_clicks=0, className="button_style"),
    ])
], className="sidebar_style")

# Define the initial content as an empty div
initial_content = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='initial-content'),
], className="content_style")


# Define the app layout
app.layout = html.Div([sidebar, initial_content])

# Callback to update the initial content when "First" button is clicked
@app.callback(
    Output('initial-content', 'children'),
    [Input('pg1', 'n_clicks'),
     Input('pg2', 'n_clicks'),
     Input('pg3', 'n_clicks'),
     Input('pg4', 'n_clicks')]
)
def update_initial_content(n_clicks1, n_clicks2, n_clicks3, n_clicks4):
    if any([n_clicks1, n_clicks2, n_clicks3, n_clicks4]):
        button_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'pg1':
            from pages import page1
            return page1.layout
        elif button_id == 'pg2':
            from pages import world_dist
            return world_dist.layout
        elif button_id == 'pg3':
            from pages import cross_sect
            return cross_sect.layout
        elif button_id == 'pg4':
            from pages import india_specific
            return india_specific.layout
    else:
        from pages import home_page
        return home_page.layout
        

        

if __name__ == '__main__':
    app.run_server(debug=True)
