from dash import html, dcc

map_layout = [
    html.H2("Salary Distribution Map", className="text-center my-4"),
    dcc.Graph(id="salary-map")
]