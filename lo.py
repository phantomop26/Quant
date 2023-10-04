with open('nytry.txt', 'r') as file:
    stocks_to_monitor = [line.strip() for line in file]
print(stocks_to_monitor)