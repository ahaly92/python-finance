import datetime as dt

import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)


df = web.DataReader('AMZN', 'yahoo', start)
df.to_csv('amzn.csv')

df = pd.read_csv('amzn.csv', parse_dates=True, index_col=0)
df['100ma'] = df['Adj Close'].rolling(window=100).mean()
df.dropna(inplace=True)
df['100ma'].plot()
plt.show()
