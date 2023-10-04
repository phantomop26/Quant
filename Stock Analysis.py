import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Replace with your Alpha Vantage API key
api_key = 'RDJ3RCOW1TQOLSX4'

# Define the stock symbol you want to analyze
symbol = input("Stock Name: ")

# Initialize the Alpha Vantage API client
ts = TimeSeries(key=api_key, output_format='pandas')

# Retrieve historical daily data
data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')

# Reverse the DataFrame to have the oldest data first
data = data[::-1]

# Calculate and plot moving averages (e.g., 50-day and 200-day)
data['SMA50'] = data['4. close'].rolling(window=50).mean()
data['SMA200'] = data['4. close'].rolling(window=200).mean()

# Calculate and plot Relative Strength Index (RSI)
def calculate_rsi(data, window=14):
    diff = data['4. close'].diff(1)
    gain = diff.where(diff > 0, 0)
    loss = -diff.where(diff < 0, 0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

data['RSI'] = calculate_rsi(data)

# Plot the stock price along with moving averages and RSI
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['4. close'], label='Price', alpha=0.7)
plt.plot(data.index, data['SMA50'], label='SMA50', alpha=0.7)
plt.plot(data.index, data['SMA200'], label='SMA200', alpha=0.7)
plt.axhline(y=70, color='r', linestyle='--', label='Overbought (70)')
plt.axhline(y=30, color='g', linestyle='--', label='Oversold (30)')
plt.fill_between(data.index, y1=30, y2=70, color='yellow', alpha=0.2)
plt.legend()
plt.twinx()
plt.plot(data.index, data['RSI'], label='RSI', color='purple')
plt.axhline(y=70, color='r', linestyle='--')
plt.axhline(y=30, color='g', linestyle='--')
plt.ylim(0, 100)
plt.legend(loc='upper left')
plt.title(f'Quantitative Analysis of {symbol}')
plt.show()

# Print the last few rows of the data, including calculated metrics
print(data.tail())
