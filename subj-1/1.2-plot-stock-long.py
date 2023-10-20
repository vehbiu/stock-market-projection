####
## Draw long-time data plots in several years. Make a graph that can change at different time points. Plot the APPL stock chart first with daily data points for several years. 
####
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def get_stock_hist(symbol: str, years: int = None) -> pd.DataFrame:
  if not years:
    years: int = 1
  stock: yf.Ticker = yf.Ticker(symbol)
  return stock.history(period=f"{years}y")

if __name__ == "__main__":
  SYMBOL: str = "AAPL"
  YEARS: int = 5
  
  data: pd.DataFrame = get_stock_hist(SYMBOL, YEARS)

  plt.figure(figsize=(15, 6)) # make it wide
  plt.plot(data.index, data['Close'], label=f'{SYMBOL} Close Price')
  plt.title(f'{SYMBOL} Stock Price Over the Last {YEARS} Years')
  plt.xlabel('Date')
  plt.ylabel('Price (USD)')
  plt.legend()
  plt.grid(True)
  plt.show()
