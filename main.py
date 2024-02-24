import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt
import mplfinance as mpf

today = date.today()
d1 = today.strftime("%Y-%m-%d")
end_date = d1

d2 = date.today() - timedelta(days=420)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download("BTC-USD", start=start_date, end=end_date, progress=False)

data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)

correlation = data.corr()
print(correlation["Close"].sort_values(ascending=False))
