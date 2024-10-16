import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


# Set your file path using raw string
in_st = r'C:\Users\Justin\OneDrive\Desktop\Python\python_app_dev\data\IN_covid19_20-23.csv'
in_co = r'C:\Users\Justin\OneDrive\Desktop\Python\python_app_dev\data\IN_covid_report_county_historical.csv'

# Statewide dataset
in_st = pd.read_csv(in_st)
print(in_st.head())

# County dataset
in_co = pd.read_csv(in_co)
# print(in_co.head())

st_20 = rin_st = r'C:\Users\Justin\OneDrive\Desktop\Python\python_app_dev\data\IN_covid19_20-23.csv'
st_20 = pd.read_csv(st_20)

st_date = '2/26/2020'
end_date = '12/31/2020'

st_20_filtered = st_20 \
                .filter(col('DATE') >= st_date) & (col('DATE') <= end_date)
print(st_20_filtered)
