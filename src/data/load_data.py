import pandas as pd
import os

data_path = os.path.join(os.path.dirname(__file__), "../../data/processed/salaries.csv")

# Load processed salaries data
data = pd.read_csv(data_path)