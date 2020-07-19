import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pf
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

df = web.DataReader('AMZN', 'yahoo', start)

print(df.tail(6))
