from dash import html
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

# Dashboard page layout
dashboard_layout = dbc.Container([
    html.Br(),

    # Salary Card & Line Chart
    dbc.Row([
        html.Div([
            html.H4("Average Salary Over 4 Years", className="text-center"),
            dvc.Vega(id='line-chart', className="border p-3")
        ])
    ]),
    html.Br(),
    html.Br(),
    # Bar charts
    dbc.Row([

        dbc.Col(html.Div([
            html.H4("Average Salary by Company Size", className="text-center"),
            dvc.Vega(id='bar-company-size', className="border p-3")  # Placeholder
        ]), width=6),
        
        dbc.Col(html.Div([
            html.H4("Average Salary by Top 10 Job Title", className="text-center"),
            dvc.Vega(id='bar-job-title', className="border p-3")  # Placeholder
        ]), width=6),

    ], className="mb-4"),

    dbc.Row([
        dbc.Col(html.Div([
            html.H4("Average Salary by Employment Type", className="text-center"),
            dvc.Vega(id='bar-employment-type', className="border p-3")
            ]), width=6),
        
        dbc.Col(html.Div([
            html.H4("Average Salary by Experience Level", className="text-center"),
            dvc.Vega(id='bar-experience-level', className="border p-3")
        ]), width=6),
        
    ], className="mb-4")
    
], fluid=True)
