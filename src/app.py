import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

# Initialize Dash app with Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define app layout
app.layout = dbc.Container([
    html.H1("Data Science Salaries Tracker", className="text-center my-4"),  # Title

    # Filters Section
    dbc.Row([
        dbc.Col([
            html.Label("Company Location"),
            dcc.Dropdown(
                id="location-filter",
                options=[], placeholder="Select a location", multi=True
            ),
        ], width=3),

        dbc.Col([
            html.Label("Job Title"),
            dcc.Dropdown(
                id="job-filter",
                options=[], placeholder="Select a job title", multi=True
            ),
        ], width=3),

        dbc.Col([
            html.Label("Experience Level"),
            dcc.Dropdown(
                id="exp-filter",
                options=[], placeholder="Select experience level", multi=True
            ),
        ], width=3),

        dbc.Col([
            html.Label("Employment Type"),
            dcc.Dropdown(
                id="emp-filter",
                options=[], placeholder="Select employment type", multi=True
            ),
        ], width=3),
    ], className="mb-4"),  # Adds space below the filters

    # Average Salary Display
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Average Salary", className="card-title"),
                    html.H2(id="average-salary", children="150K", className="text-primary text-center")
                ])
            ], className="shadow-sm p-3")
        ], width=4),
    ], className="mb-4 justify-content-center"),  # Centers the salary card

    # Placeholder for Pie Charts (Can be replaced with text-based insights)
    dbc.Row([
        dbc.Col([
            dbc.Alert("📊 Employment Type Analysis Coming Soon!", color="info", className="text-center")
        ], width=6),
        dbc.Col([
            dbc.Alert("📊 Experience Level Analysis Coming Soon!", color="info", className="text-center")
        ], width=6),
    ]),

    # Placeholder for Bar Charts (Can be replaced with simple text summaries)
    dbc.Row([
        dbc.Col([
            dbc.Alert("📈 Salary by Company Size Coming Soon!", color="warning", className="text-center")
        ], width=4),
        dbc.Col([
            dbc.Alert("📈 Salary by Job Title Coming Soon!", color="warning", className="text-center")
        ], width=4),
        dbc.Col([
            dbc.Alert("📈 Salary by Employment Type Coming Soon!", color="warning", className="text-center")
        ], width=4),
    ], className="mt-4"),
], fluid=True)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
