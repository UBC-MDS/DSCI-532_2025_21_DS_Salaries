from dash import html, dcc
import dash_bootstrap_components as dbc


des = html.Div([
    html.H1(' '),
    html.P('The Salary Dashboard provides an interactive analysis of Data Science job salaries. The dashboard highlights average salaries while enabling dynamic exploration of salary trends across different roles and employment structures. Users can gain insights into job market patterns, helping them compare salaries and make informed career decisions.'),
    html.P("Author: Zhengling Jiang, Kexin Shi, Jingyuan Wang, Tengwei Wang"),
    html.A(
        "Github repo",
        href="https://github.com/UBC-MDS/DSCI-532_2025_21_DS_Salaries",
        target="_blank"  # Opens in a new tab
    ),
    html.P("Latest update on March 9, 2025.")
])

side_layout = dbc.Container([
    dbc.Row([
        # title
        dbc.Col(html.H1("Data Science Salaries Tracker", className="my-2"), width="auto")
    ]),
    dbc.Row([
        html.H1(' ')
    ]),
        # button
    dbc.Row([
        dbc.Col(
            dbc.ButtonGroup([
                dbc.Button("Analytics Page", id="btn-dashboard", color="primary", className="me-2 px-4 py-2"),
                dbc.Button("Map Page", id="btn-map", color="primary", className="px-4 py-2")  
            ], className="ml-auto"), width="auto", className="d-flex align-items-center ms-3"
        )
    ], className="d-flex align-items-center mb-4"),
    dbc.Row([
        html.H1(' ')
    ]),
    dbc.Row([
        html.H1(' ')
    ]),
    # card
    dbc.Row([
        dbc.Card([            
            dbc.CardBody([
                html.H4("Average Salary (Filtered)", className="card-title"),
                html.H2(id='filtered-average-salary', className="card-text"),
            ])
            ], className="shadow p-3",style = {"color":"white","backgroundColor":"#343a40"}
        ), 
    ]),
    dbc.Row([
        html.H1(' ')
    ]),
    dbc.Row([
        html.H1(' ')
    ]),
    # filter
    dbc.Row([
        dbc.Col(dcc.Dropdown(id='company-location', options=[], placeholder="Select Company Location"))
    ], className="mb-4", style = {"color":"black"}),
    dbc.Row([
        dbc.Col(dcc.Dropdown(id='experience-level', options=[], placeholder="Select Experience Level"))
    ], className="mb-4", style = {"color":"black"}),
    dbc.Row([
        dbc.Col(dcc.Dropdown(id='employment-type', options=[], placeholder="Select Employment Type"))
    ], className="mb-4", style = {"color":"black"}),


    dbc.Row([
        html.H1(' ')
    ]),
    dbc.Row([
        html.H1(' ')
    ]),
    dbc.Row([
        html.H1(' ')
    ]),
    dbc.Row([
        des
    ])
]

,fluid = True)