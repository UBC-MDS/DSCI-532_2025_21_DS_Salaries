import dash
from dash import Dash, dcc, html, callback, Output, Input
import pandas as pd
import altair as alt
from src.data.load_data import data  

def register_chart_callbacks(app):
    # callback to update card and line chart
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
            filtered_df = filtered_df[filtered_df["company_location"].isin(location)]
        if experience:
            filtered_df = filtered_df[filtered_df["experience_level"].isin(experience)]
        if employment:
            filtered_df = filtered_df[filtered_df["employment_type"].isin(employment)]

        if filtered_df.empty:
            empty_chart = alt.Chart().mark_text(
                text="No data available",
                fontSize=20
            ).properties(
                width=1100,
                height=100
            )
            return "No data available", empty_chart.to_dict()

        # Calculate average salary based on the outputs of filters
        avg_salary = filtered_df["salary_in_usd"].mean()
        avg_salary_text = f"${avg_salary:,.0f}" if not pd.isna(avg_salary) else "N/A"

        # generate line chart
        line_chart_data = (
            filtered_df.groupby("work_year")["salary_in_usd"]
            .mean()
            .reset_index()
        )

        line_chart = alt.Chart(line_chart_data).mark_line(point=True).encode(
            x=alt.X("work_year:O", axis=alt.Axis(title=None, labelAngle=0)),
            y=alt.Y("salary_in_usd:Q",
                    scale=alt.Scale(nice=True),
                    axis=alt.Axis(format="$~s", title=None)),
            tooltip=["work_year", "salary_in_usd"]
        ).properties(
            width=1300,
            height=100
        ).interactive()

        return avg_salary_text, line_chart.to_dict()

    # callback to update bar chart of employment type
    @app.callback(
        Output('bar-employment-type', 'spec'),
        Input('company-location', 'value'),
        Input('experience-level', 'value'),
        Input('employment-type', 'value')
    )
    def update_bar_chart_employment_type(location, experience, employment):
        # Filter
        filtered_df = data.copy()
        
        if location:
            filtered_df = filtered_df[filtered_df["company_location"].isin(location)]
        if experience:
            filtered_df = filtered_df[filtered_df["experience_level"].isin(experience)]
        if employment:
            filtered_df = filtered_df[filtered_df["employment_type"].isin(employment)]

        # When no data available
        if filtered_df.empty:
            empty_chart = alt.Chart().mark_text(
                text="No data available",
                fontSize=20
            ).properties(
                width=450,
                height=200
            )
            return empty_chart.to_dict()

        # Calculate average salary based on the outputs of filters
        employment_chart_data = (
            filtered_df.groupby("employment_type", as_index=False)["salary_in_usd"].mean()
        )

        # Create Altair Bar Chart
        employment_chart = alt.Chart(employment_chart_data).mark_bar().encode(
            x=alt.X("salary_in_usd:Q",
                    title="Average Salary", 
                    scale=alt.Scale(domain=[0, employment_chart_data["salary_in_usd"].max()]),  
                    axis=alt.Axis(format="~s")),
            y=alt.Y("employment_type:N", sort="-x", axis=alt.Axis(title=None)),
            tooltip=["employment_type", "salary_in_usd"]
        ).properties(
            width=450,
            height=200
        )

        return employment_chart.to_dict()

    # Callback to update the Bar Chart for Salary by Experience Level based on the filter results
    @app.callback(
        Output('bar-experience-level', 'spec'),
        Input('company-location', 'value'),
        Input('experience-level', 'value'),
        Input('employment-type', 'value')
    )
    def update_bar_chart_experience_level(location, experience, employment):
        # Filter
        filtered_df = data.copy()
        
        if location:
            filtered_df = filtered_df[filtered_df["company_location"].isin(location)]
        if experience:
            filtered_df = filtered_df[filtered_df["experience_level"].isin(experience)]
        if employment:
            filtered_df = filtered_df[filtered_df["employment_type"].isin(employment)]

        # When no data available
        if filtered_df.empty:
            empty_chart = alt.Chart().mark_text(
                text="No data available",
                fontSize=20
            ).properties(
                width=450,
                height=200
            )
            return empty_chart.to_dict()

        # Calculate average salary based on the outputs of filters
        experience_chart_data = (
            filtered_df.groupby("experience_level", as_index=False)["salary_in_usd"].mean()
        )


        # Create Altair Bar Chart
        experience_chart = alt.Chart(experience_chart_data).mark_bar().encode(
            x=alt.X("salary_in_usd:Q",
                    title="Average Salary", 
                    scale=alt.Scale(domain=[0, experience_chart_data["salary_in_usd"].max()]),  
                    axis=alt.Axis(format="~s")),
            y=alt.Y("experience_level:N", sort="-x", axis=alt.Axis(title=None)),
            tooltip=["experience_level", "salary_in_usd"]
        ).properties(
            width=450,
            height=200
        )

        return experience_chart.to_dict()


    # Callback to generate the Salary by Company Size based on filter results

    @app.callback(
        Output('bar-company-size',"spec"),
        Input('company-location', 'value'),
        Input('experience-level', 'value'),
        Input('employment-type', 'value')
    )
    def show_salary_by_size_bar(location, experience, employment):
        # Filter
        filtered_df = data.copy()
        
        if location:
            filtered_df = filtered_df[filtered_df["company_location"].isin(location)]
        if experience:
            filtered_df = filtered_df[filtered_df["experience_level"].isin(experience)]
        if employment:
            filtered_df = filtered_df[filtered_df["employment_type"].isin(employment)]

        # When no data available
        if filtered_df.empty:
            empty_chart = alt.Chart().mark_text(
                text="No data available",
                fontSize=20
            ).properties(
                width=450,
                height=200
            )
            return empty_chart.to_dict()

        # Calculate average salary based on the outputs of filters
        salary_by_size = (
            filtered_df.groupby("company_size", as_index=False)["salary_in_usd"].mean()
        )

        
        # Create Altair Bar Chart
        size_bar_chart = alt.Chart(salary_by_size).mark_bar().encode(
            x=alt.X("salary_in_usd:Q",
                    title="Average Salary", 
                    scale=alt.Scale(domain=[0, salary_by_size["salary_in_usd"].max()]),  
                    axis=alt.Axis(format="~s")),
            y=alt.Y("company_size:N",sort="-x", axis=alt.Axis(title=None)),
            tooltip=["company_size", "salary_in_usd"]
        ).properties(
            width=450,
            height=200
        )
        return size_bar_chart.to_dict()
        

    # Callback to generate bar chart for Overall Top 10 Job Title by Salary based on filtered results
    @app.callback(
        Output('bar-job-title',"spec"),
        Input('company-location', 'value'),
        Input('experience-level', 'value'),
        Input('employment-type', 'value')
    )
    def show_salary_by_title(location, experience, employment):
        # Filter
        filtered_df = data.copy()
        
        if location:
            filtered_df = filtered_df[filtered_df["company_location"].isin(location)]
        if experience:
            filtered_df = filtered_df[filtered_df["experience_level"].isin(experience)]
        if employment:
            filtered_df = filtered_df[filtered_df["employment_type"].isin(employment)]

       # When no data available
        if filtered_df.empty:
            empty_chart = alt.Chart().mark_text(
                text="No data available",
                fontSize=20
            ).properties(
                width=400,
                height=200
            )
            return empty_chart.to_dict()

        # Calculate average salary based on the outputs of filters and choose top 10
        salary_by_title = (
            filtered_df.groupby("job_title", as_index=False)["salary_in_usd"].mean()
        )
        

        top10_salary_by_title = salary_by_title.nlargest(10, "salary_in_usd")

        title_bar_chart = alt.Chart(top10_salary_by_title).mark_bar().encode(
            x=alt.X("salary_in_usd:Q",
                    title="Average Salary", 
                    scale=alt.Scale(domain=[0, top10_salary_by_title["salary_in_usd"].max()]),  
                    axis=alt.Axis(format="~s")),
            y=alt.Y("job_title:N",sort="-x", axis=alt.Axis(title=None)),
            tooltip=["job_title", "salary_in_usd"]
        ).properties(
            width=400,
            height=200
        )
        return title_bar_chart.to_dict()
