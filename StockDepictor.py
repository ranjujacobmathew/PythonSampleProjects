import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

# Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
api_key = 'BHBZIXVVF0GMPHZT'

# Function to fetch stock data using Alpha Vantage API
def get_stock_data(symbol, interval='1min', outputsize='compact'):
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=symbol, interval=interval, outputsize=outputsize)
    return data

# Function to plot stock data
def plot_stock_data(data, symbol):
    plt.figure(figsize=(10, 6))
    data['4. close'].plot(label='Close Price', title=f'Stock Price for {symbol}')
    plt.xlabel('Time')
    plt.ylabel('Stock Price (USD)')
    plt.legend()
    plt.show()

# Example: Fetching and plotting Apple Inc. (AAPL) stock data
symbol = 'AAPL'
stock_data = get_stock_data(symbol)
print(stock_data)
plot_stock_data(stock_data, symbol)