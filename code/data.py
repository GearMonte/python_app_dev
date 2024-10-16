import pandas as pd

# Set your file path using raw string
in_st = r'C:\Users\Justin\OneDrive\Desktop\Python\python_app_dev\data\IN_covid19_20-23.csv'

# Statewide dataset
in_st = pd.read_csv(in_st)
print(in_st.head())
