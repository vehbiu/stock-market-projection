####
## Overplot SMA20/SMA50, or SMA 50/SMA150. These are great indicators for stock data.	
####

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def get_stock_hist(symbol: str, years: int = None) -> pd.DataFrame:
  if not years:
    years: int = 1
  stock = yf.Ticker(symbol)
  return stock.history(period=f"{years}y")


if __name__ == "__main__":
  SYMBOL: str = 'AAPL'
  YEARS: int = 5
  data: pd.DataFrame = get_stock_hist(SYMBOL, YEARS)

  # Calculate the 20-period and 50-period Simple Moving Averages (SMA)
  # .rolling() is used to create a rolling window of the data 
  # basically just plot the data
  sma_20 = data['Close'].rolling(window=20).mean()
  sma_50 = data['Close'].rolling(window=50).mean()

  # Plot the stock price and SMAs
  plt.figure(figsize=(15, 6))
  plt.plot(data.index, data['Close'], label=f'{SYMBOL} Closing Price')
  plt.plot(data.index, sma_20, label='SMA 20')
  plt.plot(data.index, sma_50, label='SMA 50')
  # plt.plot(data.index, sma_20, label='SMA 20', linestyle=":")
  # plt.plot(data.index, sma_50, label='SMA 50', linestyle='--')

  plt.title(f'{SYMBOL} Stock Price w/ SMA20 and SMA50 | {YEARS} Years')
  plt.xlabel('Date')          # x label
  plt.ylabel('Price (USD)')   # y label
  plt.legend()                # show legend
  plt.grid(True)              # show grid to differentiate easier
  plt.show()
