import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, callback, Output, Input
import pandas as pd 
import altair as alt
import dash_vega_components as dvc

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
        dbc.Col([
            dbc.Card([            
                dbc.CardBody([
                    html.H4("Average Salary (Filtered)", className="card-title"),
                    html.H2(id='filtered-average-salary', className="card-text"),
                ])
                ], className="shadow p-3"
            ), 
            dbc.Card([            
                dbc.CardBody([
                    html.H4("Overall Average Salary", className="card-title"),
                    html.H2(id='overall-average-salary', className="card-text"),
                ])
                ], className="shadow p-3"
            )],
            width=4
        ),

        dbc.Col(
            html.Div([
                html.H4("Line Chart: Salary Over 4 Years", className="text-center"),
                dvc.Vega(id='line-chart', className="border p-3")
            ]), width=8
        )
    ]),

    # Static Charts
    dbc.Row([
        #dbc.Col(
            #dbc.Card([
            
        #], className="shadow p-3"), width=4),

        dbc.Col(html.Div([
            html.H4("Overall Salary by Company Size", className="text-center"),
            dvc.Vega(id='bar-company-size', className="border p-3")  # Placeholder
        ]), width=6),
        
        dbc.Col(html.Div([
            html.H4("Overall Top 10 Job Title by Salary", className="text-center"),
            dvc.Vega(id='bar-job-title', className="border p-3")  # Placeholder
        ]), width=6),

    ], className="mb-4"),

    dbc.Row([
        dbc.Col(html.Div([
            html.H4("Overall Salary by Employment Type", className="text-center"),
            dvc.Vega(id='bar-employment-type', className="border p-3")
            ]), width=6),
        
        dbc.Col(html.Div([
            html.H4("Overall Salary by Experience Level", className="text-center"),
            dvc.Vega(id='bar-experience-level', className="border p-3")
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

# Callback: Get options for dropdown of company location
@app.callback(
    Output('company-location', 'options'),
    Input('company-location', 'id') 
)
def set_company_location_options(_):
    unique_locations = sorted(data['company_location'].dropna().unique())
    options = [{'label': location, 'value': location} for location in unique_locations]
    return options
    
# Callback: Get options for dropdown of experience level
@app.callback(
    Output('experience-level', 'options'),
    Input('experience-level', 'id') 
)
def set_experience_level_options(_):
    unique_experience_levels = sorted(data['experience_level'].dropna().unique())
    return [{'label': level, 'value': level} for level in unique_experience_levels]

# Callback: Get options for dropdown of exployment type
@app.callback(
    Output('employment-type', 'options'),
    Input('employment-type', 'id')
)
def set_employment_type_options(_):
    unique_employment_types = sorted(data['employment_type'].dropna().unique())
    return [{'label': emp_type, 'value': emp_type} for emp_type in unique_employment_types]

# Callback to update the card and line chart based on the results of filters
@app.callback(
	Output('filtered-average-salary', 'children'),
    Output('line-chart', 'spec'),
    Input('company-location', 'value'),
    Input('experience-level', 'value'),
    Input('employment-type', 'value')
)
def update_dashboard(location, experience, employment):
    # filter
    filtered_df = data.copy()
    
    if location:
        filtered_df = filtered_df[filtered_df["company_location"] == location]
    if experience:
        filtered_df = filtered_df[filtered_df["experience_level"] == experience]
    if employment:
        filtered_df = filtered_df[filtered_df["employment_type"] == employment]

    # Calculate average salary based on the outputs of filters
    avg_salary = filtered_df["salary_in_usd"].mean()
    avg_salary_text = f"${avg_salary:,.2f}" if not pd.isna(avg_salary) else "N/A"

    # generate line chart
    line_chart_data = (
        filtered_df.groupby("work_year")["salary_in_usd"]
        .mean()
        .reset_index()
    )

    line_chart = alt.Chart(line_chart_data).mark_line(point=True).encode(
        x=alt.X("work_year:O", title="Year"),
        y=alt.Y("salary_in_usd:Q", title="Average Salary (USD)"),
        tooltip=["work_year", "salary_in_usd"]
    ).properties(
        width=800,
        height=100
    ).interactive()

    return avg_salary_text, line_chart.to_dict()

# Callback to generate the Bar Chart for Salary by Employment Type (Unfiltered)
@app.callback(
    Output('bar-employment-type', 'spec'),
    Input('bar-employment-type', 'id')  # Dummy trigger
)
def update_bar_chart_employment_type(_):
    # Aggregate: Overall average salary by employment type
    employment_chart_data = (
        data.groupby("employment_type")["salary_in_usd"]
        .mean()
        .reset_index()
    )

    if employment_chart_data.empty:
        return html.P("No data available.")

    # Create Altair Bar Chart
    employment_chart = alt.Chart(employment_chart_data).mark_bar().encode(
        x=alt.X("salary_in_usd:Q", title="Average Salary (USD)"),
        y=alt.Y("employment_type:N", title="Employment Type", sort="-x"),
        tooltip=["employment_type", "salary_in_usd"]
    ).properties(
        width=600,
        height=200
    )

    return employment_chart.to_dict()

# Callback to generate the Bar Chart for Salary by Experience Level (Unfiltered)
@app.callback(
    Output('bar-experience-level', 'spec'),
    Input('bar-experience-level', 'id')  # Dummy trigger
)
def update_bar_chart_experience_level(_):
    # Aggregate: Overall average salary by experience level
    experience_chart_data = (
        data.groupby("experience_level")["salary_in_usd"]
        .mean()
        .reset_index()
    )

    if experience_chart_data.empty:
        return html.P("No data available.")

    # Create Altair Bar Chart
    experience_chart = alt.Chart(experience_chart_data).mark_bar().encode(
        x=alt.X("salary_in_usd:Q", title="Average Salary (USD)"),
        y=alt.Y("experience_level:N", title="Experience Level", sort="-x"),
        tooltip=["experience_level", "salary_in_usd"]
    ).properties(
        width=600,
        height=200
    )

    return experience_chart.to_dict()


# Overall Salary by Company Size

@app.callback(
    Output('bar-company-size',"spec"),
    Input('bar-company-size','id')
)
def show_salary_by_size_bar(_):
    salary_by_size = data.groupby('company_size')['salary_in_usd'].mean().reset_index()
    
    size_bar_chart = alt.Chart(salary_by_size).mark_bar().encode(
        x=alt.X("salary_in_usd:Q",title = "Average Salary (USD)"),
        y=alt.Y("company_size:N",title = "Company Size",sort="-x"),
        tooltip=["company_size", "salary_in_usd"]
    ).properties(
        width=600,
        height=200
    )
    return size_bar_chart.to_dict()
    

# Overall Top 10 Job Title by Salary
@app.callback(
    Output('bar-job-title',"spec"),
    Input('bar-job-title','id')
)
def show_salary_by_title(_):
    salary_by_title = data.groupby('job_title')['salary_in_usd'].mean().reset_index()

    title_bar_chart = alt.Chart(salary_by_title).mark_bar().encode(
        x=alt.X("salary_in_usd:Q",title = "Average Salary (USD)"),
        y=alt.Y("job_title:N",title = "Job Title",sort="-x"),
        tooltip=["job_title", "salary_in_usd"]
    ).properties(
        width=600,
        height=200
    )
    return title_bar_chart.to_dict()



# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)
