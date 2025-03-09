import dash
from dash import Dash, dcc, html, callback, Output, Input
from data.load_data import data
import pandas as pd

def register_filter_callbacks(app):
    # Callback: Get options for dropdown of company location
    @app.callback(
        Output('company-location', 'options'),
        Input('company-location', 'id') 
    )
    def set_company_location_options(_):
        unique_locations = sorted(data['company_location'].dropna().unique())
        return [{'label': location, 'value': location} for location in unique_locations]

    # Callback: Get options for dropdown of experience level
    @app.callback(
        Output('experience-level', 'options'),
        Input('experience-level', 'id') 
    )
    def set_experience_level_options(_):
        unique_experience_levels = sorted(data['experience_level'].dropna().unique())
        return [{'label': level, 'value': level} for level in unique_experience_levels]

    # Callback: Get options for dropdown of employment type
    @app.callback(
        Output('employment-type', 'options'),
        Input('employment-type', 'id')
    )
    def set_employment_type_options(_):
        unique_employment_types = sorted(data['employment_type'].dropna().unique())
        return [{'label': emp_type, 'value': emp_type} for emp_type in unique_employment_types]
