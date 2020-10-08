from sqlalchemy import create_engine
import pymysql
import pandas as pd
import matplotlib.pyplot as plt

credentials = 'mysql+pymysql://deroweb:tgfykf348666666@127.0.0.1/deroweb_clima'

# read in your SQL query results using pandas
dataframe = pd.read_sql("""
            SELECT *
            FROM log
            """, con = credentials)
# return your first five rows

print(dataframe.head())
print(dataframe.tail())
dataframe.to_csv('log.csv')

plt.figure