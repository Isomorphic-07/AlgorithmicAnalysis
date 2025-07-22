import numpy as np
import pandas as pd
import pandas_ta as ta
import requests 
import xlsxwriter
import math
from scipy.stats import linregress

df = pd.read_csv('AUDUSD.csv')
print(df.tail()) #Prints out last few rows

#We now want to check if any zero volumes are available

indexZeros = df[ df['Volume'] == 0].index 
# df[df['volume']==0] Filters the data frame to only be rows
# where the volume is 0
# .index extracts index labels of the rows

df.drop(indexZeros, inplace = True)
df.loc[(df['Volume'] == 0)] #.loc returns rows where mask is true
df.isna().sum() #Checks for any missing (NaNs) values in each column and sums it

#df.ta.indicators() tells us all the indicators in technical analysis
#help(ta.atr)

df['ATR'] = df.ta.atr(length = 20)
df['RSI'] = df.ta.rsi()
df['Average'] = df.ta.midprice(length=1)
df["MA40"] = df.ta.sma(length = 40).iloc[:, 1]
df["MA80"] = df.ta.sma(length = 80).iloc[:, 1]
df['MA160'] = df.ta.sma(length = 160).iloc[:, 1]


def get_slope(array):
    y = np.array(array)
    x = np.arange(len(y)) #allocates x alues with sequential indices for time series data
    slope, intercept, r_alue, p_value, std_err = linregress(x,y)
    return slope

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
backrollingN = 6 # Rolling window of 6 periods
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
df['slopeMA40'] = df['MA40'].rolling(window=backrollingN).apply(get_slope, raw=True)
df['slopeMA80'] = df['MA80'].rolling(window=backrollingN).apply(get_slope, raw=True)
df['slopeMA160'] = df['MA160'].rolling(window=backrollingN).apply(get_slope, raw=True)
df['AverageSlope'] = df['Average'].rolling(window=backrollingN).apply(get_slope, raw=True)
df['RSISlope'] = df['RSI'].rolling(window=backrollingN).apply(get_slope, raw=True)
# rolling().apply(get_slope, raw=True) function applies the get_slope() function to each rolling window.

print(df.tail())
