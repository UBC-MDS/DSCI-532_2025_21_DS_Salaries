import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, callback, Output, Input, State
import sys
import os

# set relative path
dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(dir)

from src.callbacks.filters import register_filter_callbacks
from src.callbacks.charts import register_chart_callbacks
from src.callbacks.map import register_map_callbacks
from src.components.sidebar import side_layout
from src.components.charts import dashboard_layout
from src.components.map import map_layout

# Initialize Dash app with Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],title="Salaries Tracker")
server = app.server

# Define App Layout (Navigation + Page Content)
app.layout = dbc.Container([

    # Top Section: Title & Navigation Buttons (Fixed)
    dbc.Row([
        dbc.Col([
            side_layout
            ], width = 3
        ,style={
            # 'display': 'flex',
            #'flexDirection': 'column',  # Stack children vertically
            #'position': 'fixed',  # Fix the sidebar on the left
            'top': '0',  # Make sure it starts at the top of the page
            'left': '0',  # Fix it to the left of the page
            'minHeight': '100vh',  # Ensure the sidebar takes full height of the page
            'overflowY': 'auto',  # Allow the sidebar to scroll if content exceeds viewport height
            'padding-left': 10,
            'color': 'white', 
            'backgroundColor': "#343a40", 
            "box-sizing": "border-box",  # Include padding and borders in element's total width and height
        }
        ),
        dbc.Col([
            # Main Content (Changes with Page)
            html.Div(id="page-content")
            ],width = 9
        )
    ])

], fluid=True)

whole_layout = dbc.Container([
    dbc.Row([
        dbc.Col([side_layout],width=3),
        dbc.Col([dashboard_layout],width=9)
    ])
])



# Callback to handle page navigation
@app.callback(
    Output("page-content", "children"),
    [Input("btn-dashboard", "n_clicks"),
     Input("btn-map", "n_clicks")]
)
def display_page(btn_dashboard, btn_map):
    ctx = dash.callback_context

    # Default Page
    if not ctx.triggered:
        return dashboard_layout
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "btn-map":
        return map_layout
    else:
        return dashboard_layout
    
# Callback to toggle About section visibility
@callback(
    Output("collapse-about", "is_open"),
    Input("toggle-about", "n_clicks"),
    State("collapse-about", "is_open")
)
def toggle_about(n, is_open):
    if n:
        return not is_open
    return is_open

# Register map callbacks
register_map_callbacks(app)

# Register filter callbacks
register_filter_callbacks(app)

# Register chart callbacks
register_chart_callbacks(app)


# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
