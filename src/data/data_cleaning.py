import pycountry
import pandas as pd
import os

# Read data
data = pd.read_csv('data/raw/ds_salaries.csv')

# Rename the 
data['experience_level'] = data['experience_level'].replace({
    'SE': 'Senior',
    'EN': 'Entry-level',
    'EX': 'Executive',
    'MI': 'Mid-level',
})

# Rename the employment type
data['employment_type'] = data['employment_type'].replace({
    'FL': 'Freelance',
    'CT': 'Contract',
    'FT' : 'Full-time',
    'PT' : 'Part-time'
})

# Rename the company size
data['company_size'] = data['company_size'].replace({
    'S': 'SMALL',
    'M': 'MEDIUM',
    'L' : 'LARGE',
})

# Convert ISO 3166 country code to country name
country_dict = {c.alpha_2: c.name for c in pycountry.countries}
data['company_location'] = data['company_location'].map(country_dict)

# Select the 10 most frequently occuring job titles, and the rest are renamed to others
top_10_jobs = data['job_title'].value_counts().nlargest(10).index  # Top 10 by frequency
data.loc[~data['job_title'].isin(top_10_jobs), 'job_title'] = 'Other'

print(data['job_title'].value_counts())

def compute_salary_ranges(df):
    bins = [0, 50000, 100000, 150000, 200000, df["salary_in_usd"].max()]  
    labels = ["<50K", "50K-100K", "100K-150K", "150K-200K", ">200K"] 
    df["salary_range"] = pd.cut(df["salary_in_usd"], bins=bins, labels=labels, include_lowest=True)
    return df

# Apply salary range computation
data = compute_salary_ranges(data)

print(data.head())

processed_data_path = "data/processed/salaries.parquet" 

os.makedirs("data/processed", exist_ok=True)

data.to_parquet(processed_data_path, index=False) 

print(f"Processed data saved successfully at: {processed_data_path}")
