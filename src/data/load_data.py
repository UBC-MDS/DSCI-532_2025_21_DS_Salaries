import pandas as pd
import os

data_path = os.path.join(os.path.dirname(__file__), "../../data/processed/salaries.parquet") 

data = pd.read_parquet(data_path)

print("Data loaded successfully!")

print(data.head())