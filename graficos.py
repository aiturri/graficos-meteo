from sqlalchemy import create_engine
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import datetime

#Transforma de timedelta a str
def splitter(td):
  td = str(td).split(' ')[-1:][0]
  return td

#Credenciales MySQL
credentials = 'mysql+pymysql://deroweb:tgfykf348666666@127.0.0.1/deroweb_clima'

fecha_inicio = datetime.date.today()
fecha_fin = datetime.date.today()


# read in your SQL query results using pandas
dataframe = pd.read_sql("""
            SELECT LogTime, Temp, Humidity, Dewpoint, ApparentTemp, Windspeed,  Windgust, Windbearing, TodayRainSoFar, Pressure FROM log WHERE LogDate between '%s' and '%s' order by LogDate, LogTime
            """ % (fecha_inicio, fecha_fin), con = credentials, parse_dates='None')

#Transformo los timedelta en str
dataframe['LogTime'] = dataframe['LogTime'].apply(splitter)

print(dataframe)
print (dataframe.dtypes)

#Guardo a un archivo
#dataframe.to_csv('log.csv')

#plt.figure
