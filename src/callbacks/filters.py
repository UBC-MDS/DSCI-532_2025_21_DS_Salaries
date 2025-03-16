import dash
from dash import Dash, dcc, html, callback, Output, Input
from src.data.load_data import data  
import pandas as pd

def register_filter_callbacks(app):
    """
    Registers all callback functions related to filtering in the dashboard.

    Parameters:
    - app (Dash): The Dash application instance.
    """
    
    @app.callback(
        Output('company-location', 'options'),
        Input('company-location', 'id') 
    )
    def set_company_location_options(_):
        """
        Generates dropdown options for selecting company locations.

        Parameters:
        - _ (str): The ID of the company-location dropdown (not used in processing).

        Returns:
        - list: A list of dictionaries containing unique company locations with labels and values.
        """
        
        unique_locations = sorted(data['company_location'].dropna().unique())
        return [{'label': location, 'value': location} for location in unique_locations]
    

    # Callback: Get options for dropdown of experience level
    @app.callback(
        Output('experience-level', 'options'),
        Input('experience-level', 'id') 
    )
    def set_experience_level_options(_):
        """
        Generates dropdown options for selecting experience levels.

        Parameters:
        - _ (str): The ID of the experience-level dropdown (not used in processing).

        Returns:
        - list: A list of dictionaries containing unique experience levels with labels and values.
        """
        unique_experience_levels = sorted(data['experience_level'].dropna().unique())
        return [{'label': level, 'value': level} for level in unique_experience_levels]

    # Callback: Get options for dropdown of employment type
    @app.callback(
        Output('employment-type', 'options'),
        Input('employment-type', 'id')
    )
    def set_employment_type_options(_):
        """
        Generates dropdown options for selecting employment types.

        Parameters:
        - _ (str): The ID of the employment-type dropdown (not used in processing).

        Returns:
        - list: A list of dictionaries containing unique employment types with labels and values.
        """
        unique_employment_types = sorted(data['employment_type'].dropna().unique())
        return [{'label': emp_type, 'value': emp_type} for emp_type in unique_employment_types]
    
    # Callback: Reset all filters when button is clicked
    @app.callback(
        [
            Output('company-location', 'value'),
            Output('experience-level', 'value'),
            Output('employment-type', 'value')
        ],
        Input('reset-filters', 'n_clicks'),
        prevent_initial_call=True
    )
    def reset_filters(n_clicks):
        """
        Resets all filter dropdowns when the reset button is clicked.

        Parameters:
        - n_clicks (int): The number of times the reset button has been clicked.

        Returns:
        - tuple: None values for each filter dropdown to reset them to no selection.
        """
        return None, None, None  # Reset all dropdowns to no selection
