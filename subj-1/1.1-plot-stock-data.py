####
## Get data with python code. Extract daily and hourly stock market data and see changes. Show me in plots various ways. (Found API)
####

import warnings
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plot
from yfinance import Ticker

# yFinanace SDK gives an error, simply ingore all errors
warnings.simplefilter(action="ignore")

def get_stock_data(symbol: str, interval: str = None) -> pd.DataFrame:
  if interval is None:
    interval: str = "1d"
  stock: Ticker = yf.Ticker(symbol)
  return stock.history(interval=interval)


if __name__ == "__main__":
  SYMBOL: str = "AAPL"
  daily_data: pd.DataFrame = get_stock_data(SYMBOL)
  print(daily_data.size)
  hourly_data: pd.DataFrame = get_stock_data(SYMBOL, "1h")

  daily_data["Close"].plot(title=f"{SYMBOL} Daily Close Price")
  plot.grid(True)
  plot.show()

  hourly_data["Close"].plot(title=f"{SYMBOL} Hourly Close Price")
  plot.grid(True)
  plot.show()
