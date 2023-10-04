import requests
import json
import time

# Replace with your Alpha Vantage API key
api_key = 'RDJ3RCOW1TQOLSX4'

# Alpha Vantage API URL for real-time stock data (delayed)
base_url = 'https://www.alphavantage.co/query'

# Define the criteria for suggesting stocks (example: price change percentage)
price_change_threshold = 1.0  # Minimum price change percentage threshold

def get_realtime_stock_data(symbol):
    """
    Get delayed real-time stock data
     for a given symbol from Alpha Vantage.
    """
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',  # You can adjust the interval as needed
        'apikey': api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract the latest data point
    latest_data = next(iter(data.get('Time Series (1min)', {}).values()), None)

    return latest_data

def suggest_stocks():
    """
    Suggest stocks based on predefined criteria.
    """
    while True:
        try:
            # You can replace these with your own list of stock symbols to monitor
            stocks_to_monitor = ['GOOGL']

            for symbol in stocks_to_monitor:
                latest_data = get_realtime_stock_data(symbol)
                if latest_data:
                    latest_open = float(latest_data.get('1. open', 0))
                    latest_close = float(latest_data.get('4. close', 0))

                    # Calculate the price change percentage
                    price_change_percent = ((latest_close - latest_open) / latest_open) * 100

                    # Check if the price change percentage exceeds the threshold
                    if price_change_percent >= price_change_threshold:
                        print(f'Suggested: Buy {symbol} (Price Change: {price_change_percent:.2f}%)')

            time.sleep(60)  # Check every minute (adjust as needed)
        except KeyboardInterrupt:
            # Stop the script with Ctrl+C
            break

if __name__ == "__main__":
    suggest_stocks()
