# import dash
# from dash import Dash, html, dcc

# app = Dash(__name__, use_pages=True)

# app.layout = html.Div([
#     html.H1('Multi-page app with Dash Pages'),
#     html.Div([
#         html.Div(
#             dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
#         ) for page in dash.page_registry.values()
#     ]),
#     dash.page_container
# ])

# if __name__ == '__main__':
#     app.run(debug=True)

import dash
from dash import Dash, html, dcc, Output, Input
from dash.exceptions import PreventUpdate

app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True)

# Define the sidebar content
sidebar = html.Div([
    html.Div([
        html.Button('First', id='submit-val', n_clicks=0, className="button_style"),
        html.Button('Second', id='submit-val2', n_clicks=0, className="button_style"),
        html.Button('Third', id='submit-val3', n_clicks=0, className="button_style"),
        html.Button('Fourth', id='submit-val4', n_clicks=0, className="button_style"),
    ])
], className="sidebar_style")

# Define the initial content as an empty div
initial_content = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='initial-content'),
], className="content_style")


# Define the app layout
app.layout = html.Div([sidebar, initial_content])

# # # Define the content to be displayed when "First" button is clicked
# content = html.Div([
#     html.H1('Multi-page app with Dash Pages'),
#     html.Div([
#         html.Div(
#             dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
#         ) for page in dash.page_registry.values()
#     ]),
#     dash.page_container
# ], className="content_style")

# Callback to update the initial content when "First" button is clicked
@app.callback(
    Output('initial-content', 'children'),
    [Input('submit-val', 'n_clicks'),
     Input('submit-val2', 'n_clicks'),
     Input('submit-val3', 'n_clicks'),
     Input('submit-val4', 'n_clicks')]
)
def update_initial_content(n_clicks1, n_clicks2, n_clicks3, n_clicks4):
    if any([n_clicks1, n_clicks2, n_clicks3, n_clicks4]):
        button_id = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'submit-val':
            from pages import world_dist
            return world_dist.layout
        elif button_id == 'submit-val2':
            from pages import india_specific
            return india_specific.layout
            pass
        elif button_id == 'submit-val3':
            from pages import cross_sect
            return cross_sect.layout
            pass
        # elif button_id == 'submit-val4':
        #     # Render layout for the fourth page
        #     pass
    else:
        return []
        

        

if __name__ == '__main__':
    app.run_server(debug=True)
