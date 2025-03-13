import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, callback, Output, Input
from src.data.load_data import data
import joblib

memory = joblib.Memory("tmp", verbose=0)


def register_map_callbacks(app):
    @app.callback(
        Output("salary-map", "figure"),
        Input("salary-map", "id")
    )
    @memory.cache()  # Apply caching here
    def generate_salary_map(_):
        avg_salary_by_location = data.groupby("company_location")["salary_in_usd"].mean().reset_index()
        fig = px.choropleth(
            avg_salary_by_location,
            locations="company_location",
            locationmode="country names",
            color="salary_in_usd",
            color_continuous_scale="Viridis",
            title="Average Salary by Company Location",
            labels={"salary_in_usd": "Average Salary (USD)"},
        )
        fig.update_geos(showcoastlines=True, showland=True, fitbounds="locations")
        fig.update_layout(margin={"r":0, "t":50, "l":0, "b":0})
        return fig
