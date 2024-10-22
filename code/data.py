import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


# Set your file path using raw string
in_st = r'C:\Users\Justin\OneDrive\Desktop\Python\python_app_dev\data\IN_covid19_20-23.csv'
# in_co = r'C:\Users\Justin\OneDrive\Desktop\Python\python_app_dev\data\IN_covid_report_county_historical.csv'

# Statewide dataset
in_st = pd.read_csv(in_st)
# print(in_st.head())

# County dataset
# in_co = pd.read_csv(in_co)
# print(in_co.head())

# spark = SparkSession.builder.appName("IN_State_Covid_data").getOrCreate()
# st_20 = spark.read.csv(r'C:\Users\Justin\OneDrive\Desktop\Python\python_app_dev\data\IN_covid19_20-23.csv', header=True, inferSchma=True)

# # st_date = '2\26\2020'
# # end_date = '12\31\2020'
# st_date = '2\26\2020'
# end_date = '12\31\2020'

# st_20 = st_20.filter(col('DATE') >= st_date) & (col('DATE') <= end_date)
# # st_20.show()
