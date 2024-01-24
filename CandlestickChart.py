import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import datetime as dt
import numpy as np
# Generate random financial data for demonstration
np.random.seed(42)
date_today = dt.datetime.now()
days = pd.date_range(date_today, date_today + pd.DateOffset(10), freq='B')
data = {'Open': np.random.rand(len(days)),
        'High': np.random.rand(len(days)),
        'Low': np.random.rand(len(days)),
        'Close': np.random.rand(len(days))}
df = pd.DataFrame(data, index=days)

# Convert the date to the mdates format
df['Date'] = df.index.map(mdates.date2num)
ohlc = df[['Date', 'Open', 'High', 'Low', 'Close']].values

fig, ax = plt.subplots()
candlestick_ohlc(ax, ohlc, width=0.6, colorup='green', colordown='red')
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.title('Candlestick Chart')
plt.show()

