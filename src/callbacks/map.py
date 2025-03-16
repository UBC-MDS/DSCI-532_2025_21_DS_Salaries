import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, callback, Output, Input
from src.data.load_data import data
import joblib

memory = joblib.Memory("tmp", verbose=0)


def register_map_callbacks(app):
    @app.callback(
        Output("salary-map", "figure"),
        Input('company-location', 'value'),
        Input('experience-level', 'value'),
        Input('employment-type', 'value')
    )
    @memory.cache()  # Apply caching here
    def generate_salary_map(location, experience, employment):
        
        filtered_df = data.copy()
        
        # apply filters
        if location:
            filtered_df = filtered_df[filtered_df["company_location"].isin(location)]
        if experience:
            filtered_df = filtered_df[filtered_df["experience_level"].isin(experience)]
        if employment:
            filtered_df = filtered_df[filtered_df["employment_type"].isin(employment)]
            
        # when data is not available
        if filtered_df.empty:
            return px.choropleth(title="No Data Available") 
            
        avg_salary_by_location = filtered_df.groupby("company_location")["salary_in_usd"].mean().reset_index()
        
        # dynamic title based on filters
        title_parts = ["Average Salary"]
        if location:
            title_parts.append(f"in {location}")
        if experience:
            title_parts.append(f"for {experience} experience")
        if employment:
            title_parts.append(f"({employment})")
            
        title = " ".join(title_parts)
        
        fig = px.choropleth(
            avg_salary_by_location,
            locations="company_location",
            locationmode="country names",
            color="salary_in_usd",
            color_continuous_scale="Viridis",
            title=title,
            labels={"salary_in_usd": "Average Salary (USD)",
                    "experience_level": "Experience Level",
                    "employment_type": "Employment Type"},
        )
        fig.update_geos(showcoastlines=True, showland=True, fitbounds="locations")
        fig.update_layout(margin={"r":0, "t":50, "l":0, "b":0})
        return fig
