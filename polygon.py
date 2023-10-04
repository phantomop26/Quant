import requests
from datetime import datetime, timedelta



API_KEY = 'TLDFVc8Znf2AyZ1wnTEAdd318gAdC_c0'
BASE_URL = 'https://api.polygon.io/v2'

start_date = '2021-01-01'
end_date = '2022-12-31'
symbol=['AAPL', 'MSFT', 'AMZN', 'GOOGL','JNJ', 'JPM', 'V', 'PG', 'WMT', 'KO', 'PFE', 'T', 'HD', 'INTC', 'VZ', 'MRK', 'UNH', 'CVX', 'ORCL', 'CRM', 'XOM', 'BAC', 'TSLA', 'ADBE', 'CSCO', 'NFLX', 'CMCSA', 'NKE', 'ABBV', 'COST', 'TMUS', 'PYPL', 'NVDA', 'MCD', 'TMO', 'AEP', 'AIG', 'BA', 'PM', 'ABT', 'GS', 'MMM', 'COP', 'PEP', 'CAT', 'CVS', 'SBUX', '', '']

for i in range(len(symbol)):
    sym=symbol[i]
    endpoint = f'/aggs/ticker/{sym}/range/1/day/{start_date}/{end_date}'

    # Build the URL with your API key
    url = f'{BASE_URL}{endpoint}?apiKey={API_KEY}'

    # Send the GET request to Polygon's API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Process the data as needed
        print(sym," :",data)

   