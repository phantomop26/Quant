import pandas as pd
import pandas_ta as ta
import yfinance as yf
from datetime import datetime, timedelta

# Replace with your stock symbol, start date, and end date


symbol=['AAPL', 'MSFT', 'AMZN', 'GOOGL','JNJ', 'JPM', 'V', 'PG', 'WMT', 'KO', 'PFE', 'T', 'HD', 'INTC', 'VZ', 'MRK', 'UNH', 'CVX', 'ORCL', 'CRM', 'XOM', 'BAC', 'TSLA', 'ADBE', 'CSCO', 'NFLX', 'CMCSA', 'NKE', 'ABBV', 'COST', 'TMUS', 'PYPL', 'NVDA', 'MCD', 'TMO', 'AEP', 'AIG', 'BA', 'PM', 'ABT', 'GS', 'MMM', 'COP', 'PEP', 'CAT', 'CVS', 'SBUX', '', '']
start_date = '2021-01-01'
end_date = '2022-12-31'

# Download historical stock data from Yahoo Finance
for i in range(len(symbol)):
    sym=symbol[i]
    data = yf.download(sym, start=start_date, end=end_date)

    # Calculate moving averages (e.g., 50-day and 200-day)
    data['SMA50'] = ta.sma(data['Close'], length=50)
    data['SMA200'] = ta.sma(data['Close'], length=200)

    # Strategy: Buy when the 50-day MA crosses above the 200-day MA, sell when the opposite happens
    data['Signal'] = 0
    data.loc[data['SMA50'] > data['SMA200'], 'Signal'] = 1
    data.loc[data['SMA50'] < data['SMA200'], 'Signal'] = -1

    # Calculate daily returns
    data['Returns'] = data['Close'].pct_change()

    # Determine whether to buy, hold, or sell based on the signal
    data['Action'] = 'Hold'
    data.loc[data['Signal'] == 1, 'Action'] = 'Buy'
    data.loc[data['Signal'] == -1, 'Action'] = 'Sell'

    # Print the DataFrame with buy/sell signals

    # Calculate cumulative returns if following the strategy
    cumulative_returns = (1 + data[data['Action'] == 'Buy']['Returns']).cumprod()
    output= cumulative_returns.iloc[-1]

    if output>1:
        print(sym,": Buy or Hold")
    else:
        print(sym,": Sell")

