
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget
import pandas as pd
import pandas_ta as ta
import yfinance as yf
from datetime import datetime, timedelta


current= datetime.now()
start_date = current - timedelta(days=1)
end_date = start_date - timedelta(days=365 * 2)
start_date = start_date.strftime("%Y-%m-%d")
end_date=end_date.strftime("%Y-%m-%d")

symbol=['AAPL']
# Download historical stock data from Yahoo Finance
data = yf.download(symbol, start=start_date, end=end_date)

data['Signal'] = 0
    # Calculate moving averages (e.g., 50-day and 200-day)
data['SMA50'] = ta.sma(data['Close'], length=50)
data['SMA200'] = ta.sma(data['Close'], length=200)
print('x')

    # Strategy: Buy when the 50-day MA crosses above the 200-day MA, sell when the opposite happens

data.loc[data['SMA50'] > data['SMA200'], 'Signal'] = 1
data.loc[data['SMA50'] < data['SMA200'], 'Signal'] = -1

    # Calculate daily returns
data['Returns'] = data['Close'].pct_change()
print('x')

    # Determine whether to buy, hold, or sell based on the signal
data['Action'] = 'Hold'
data.loc[data['Signal'] == 1, 'Action'] = 'Buy'
data.loc[data['Signal'] == -1, 'Action'] = 'Sell'
print('x')

    # Print the DataFrame with buy/sell signals
    #print(data[['Close', 'SMA50', 'SMA200', 'Signal', 'Action']])
    # Calculate cumulative returns if following the strategy
cumulative_returns = (1 + data[data['Action'] == 'Buy']['Returns']).cumprod()
data=cumulative_returns.iloc[-1]
print('x')

if data>1:
    print(str(i)+" : "+"Buy or Hold")
else:     
    print(str(i)+" : "+"Sell")
