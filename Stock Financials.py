import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from yahoo_fin import stock_info as si

# Replace with your Alpha Vantage API key
api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'

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

# Plot the stock price along with moving averages
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['4. close'], label='Price', alpha=0.7)
plt.plot(data.index, data['SMA50'], label='SMA50', alpha=0.7)
plt.plot(data.index, data['SMA200'], label='SMA200', alpha=0.7)
plt.axhline(y=70, color='r', linestyle='--', label='Overbought (70)')
plt.axhline(y=30, color='g', linestyle='--', label='Oversold (30)')
plt.fill_between(data.index, y1=30, y2=70, color='yellow', alpha=0.2)
plt.legend()
plt.title(f'Stock Analysis of {symbol}')
plt.show()

# Fetch financial data from Yahoo Finance using the yahoo_fin library
# For example, you can retrieve the market cap and P/E ratio
market_cap = si.get_quote_table(symbol)['Market Cap']
pe_ratio = si.get_quote_table(symbol)['PE Ratio (TTM)']

# Display financial data
print(f"Market Cap: {market_cap}")
print(f"P/E Ratio (TTM): {pe_ratio}")
