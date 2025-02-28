import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, callback, Output, Input
import pandas as pd 
import altair as alt

# Initialize Dash app with Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Read processed data
data = pd.read_csv('data/processed/salaries.csv')

# Define app layout
app.layout = dbc.Container([
    html.H1("Data Science Salaries Tracker", className="text-center my-4"),  # Title
    
    # Filters
    dbc.Row([
        dbc.Col(dcc.Dropdown(id='company-location', options=[], placeholder="Select Company Location"), width=4),
        dbc.Col(dcc.Dropdown(id='experience-level', options=[], placeholder="Select Experience Level"), width=4),
        dbc.Col(dcc.Dropdown(id='employment-type', options=[], placeholder="Select Employment Type"), width=4),
    ], className="mb-4"),

    # Filtered Charts: Salary Card & Line Chart
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Average Salary (Filtered)", className="card-title"),
                html.H2(id='filtered-average-salary', className="card-text"),
            ])
        ], className="shadow p-3"), width=4),

        dbc.Col(html.Div([
            html.H4("Line Chart: Salary Over 4 Years", className="text-center"),
            html.Div(id='line-chart', className="border p-3")  # Placeholder
        ]), width=8),
    ], className="mb-4"),

    # Static Charts
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Overall Average Salary", className="card-title"),
                html.H2(id='overall-average-salary', className="card-text"),
            ])
        ], className="shadow p-3"), width=4),

        dbc.Col(html.Div([
            html.H4("Bar Chart: Salary by Company Size", className="text-center"),
            html.Div(id='bar-company-size', className="border p-3")  # Placeholder
        ]), width=4),
        
        dbc.Col(html.Div([
            html.H4("Bar Chart: Salary by Job Title (Top 10)", className="text-center"),
            html.Div(id='bar-job-title', className="border p-3")  # Placeholder
        ]), width=4),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(html.Div([
            html.H4("Bar Chart: Salary by Employment Type", className="text-center"),
            html.Div(id='bar-employment-type', className="border p-3")  # Placeholder
        ]), width=6),
        
        dbc.Col(html.Div([
            html.H4("Bar Chart: Salary by Experience Level", className="text-center"),
            html.Div(id='bar-experience-level', className="border p-3")  # Placeholder
        ]), width=6),
        
    ], className="mb-4"),


], fluid=True)

# Calculate the overall average salary
overall_avg_salary = data['salary_in_usd'].mean()

# Callback to update the card of overall average salary
@callback(
    Output('overall-average-salary', 'children'),
    Input('overall-average-salary', 'id')  
)
def update_overall_salary(_):
    return f"${overall_avg_salary:,.2f}"

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
