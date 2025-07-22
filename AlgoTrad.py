import yfinance as yf
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


ticker = ["SPY", "AAPL", "KO"]
stocks = yf.download(ticker, start = "2010-01-01", end = "2020-01-01")
print(stocks)
print(stocks.head())
print(stocks.info())
stocks.to_csv("stocksYT.csv")
stocks = pd.read_csv("stocksYT.csv", header = [0,1], index_col = [0],
                     parse_dates = [0])

#convert multi index to one tuple
"""
stocks.columns = stocks.columns.to_flat_index()
print(stocks)

#reverses column change
stocks.columns = pd.MultiIndex.from_tuples(stocks.columns)
print(stocks.describe()) #Gives all statistical data
close = stocks.loc[:,"Close"].copy() #filters so that only the Close values
print(close)

plt.style.use("seaborn")
close.plot(figsize = (15,8), fontsize = 12)
"""