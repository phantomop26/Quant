import sys
import pandas as pd
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from qtpy.QtGui import QTextCursor

# Replace with your Polygon API key
api_key = 'TLDFVc8Znf2AyZ1wnTEAdd318gAdC_c0'

# Define the stock symbol you want to retrieve data for
symbol=['AAPL', 'MSFT', 'AMZN', 'GOOGL','JNJ', 'JPM', 'V', 'PG', 'WMT', 'KO', 'PFE', 'T', 'HD', 'INTC', 'VZ', 'MRK', 'UNH', 'CVX', 'ORCL', 'CRM', 'XOM', 'BAC', 'TSLA', 'ADBE', 'CSCO', 'NFLX', 'CMCSA', 'NKE', 'ABBV', 'COST', 'TMUS', 'PYPL', 'NVDA', 'MCD', 'TMO', 'AEP', 'AIG', 'BA', 'PM', 'ABT', 'GS', 'MMM', 'COP', 'PEP', 'CAT', 'CVS', 'SBUX', '', '']


class StockDataApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Polygon API Stock Data")
        self.setGeometry(1000, 1000, 6000, 4000)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.setAlignment(Qt.AlignTop)

        self.fetch_button = QPushButton("Fetch Stock Data", self)
        self.fetch_button.clicked.connect(self.fetch_stock_data)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.fetch_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def fetch_stock_data(self):
        for i in range(len(symbol)):
            sym=symbol[i]
            try:
                # Fetch real-time stock data from Polygon API
                url = f'https://api.polygon.io/v1/last/stocks/{sym}?apiKey={api_key}'
                response = requests.get(url)
                data = response.json()

                if 'last' in data:
                    last_price = data['last']['price']
                    volume = data['last']['size']

                    # Display the real-time stock data in the text area
                    self.text_edit.append(f"Symbol: {symbol}")
                    self.text_edit.append(f"Last Price: ${last_price:.2f}")
                    self.text_edit.append(f"Volume: {volume}")
                    self.text_edit.moveCursor(QTextCursor.End)
            except Exception as e:
                self.text_edit.append(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockDataApp()
    window.show()
    sys.exit(app.exec_())
