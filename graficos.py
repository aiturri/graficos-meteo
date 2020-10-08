from sqlalchemy import create_engine
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import datetime

credentials = 'mysql+pymysql://deroweb:tgfykf348666666@127.0.0.1/deroweb_clima'

fecha_inicio = datetime.date.today()
fecha_fin = datetime.date.today()

print("""SELECT LogTime, Temp, Humidity, Dewpoint, ApparentTemp FROM log WHERE LogDate between '%s' and '%s' order by LogDate, LogTime""" % (fecha_inicio, fecha_fin))
