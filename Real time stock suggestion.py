from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget
import pandas as pd
import pandas_ta as ta
import yfinance as yf
from datetime import datetime, timedelta
class StockSuggestionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Suggestion App")
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)


        self.refresh_button = QPushButton("Refresh Suggestions", self)
        self.refresh_button.clicked.connect(self.update_suggestions)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.refresh_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
    def stock_names(self):
        with open('stock.txt', 'r') as file:
            stocks_to_monitor = [line.strip() for line in file]
        return stocks_to_monitor
    def update_suggestions(self):
        # Implement your stock analysis and update suggestions in the QTextEdit
        suggestions = self.calculate_stock_suggestions()
        self.text_edit.setPlainText("\n".join(suggestions))

    def calculate_stock_suggestions(self):
        # Implement your stock analysis logic here
        # Example: return a list of suggested stocks
        for i in self.stock_names():
            num=self.data_evaluate(i)
            if num>1:
                return str(i)+" : "+"Buy or Hold"
            else:     
                return str(i)+" : "+"Sell"
    def data_evaluate(self,symbol):
        symbol = str(symbol)
        start_date = datetime.datetime.now()
        end_date = start_date - datetime.timedelta(days=365 * 2)


        # Download historical stock data from Yahoo Finance
        data = yf.download(symbol, start=start_date, end=end_date)

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
        #print(data[['Close', 'SMA50', 'SMA200', 'Signal', 'Action']])
        # Calculate cumulative returns if following the strategy
        cumulative_returns = (1 + data[data['Action'] == 'Buy']['Returns']).cumprod()
        print(cumulative_returns.iloc[-1])
        return cumulative_returns.iloc[-1]


if __name__ == "__main__":
    app = QApplication([])
    window = StockSuggestionApp()
    window.show()
    app.exec_()
#ADD lolousdfj and if it is greater than 1 dollar buy it and hold or sell, 


