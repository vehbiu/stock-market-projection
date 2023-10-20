# Introduce and plot Bollinger Bands, RSI (Relative Strength Index), and MACD (Moving Average Convergence Divergence).
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

STOCK: str = 'META'

def get_bollinger_bands(df: pd.DataFrame, window: int = 20, num_of_std: int = 2) -> pd.DataFrame:
  # Upper band = 20-day SMA + (20-day SD x 2) 
  # Middle band = 20-day SMA. 
  # Lower band = 20-day SMA – (20-day SD x 2)
  rolling_mean: pd.Series = df['Close'].rolling(window).mean()
  rolling_std: pd.Series = df['Close'].rolling(window).std()
  df['Bollinger High'] = rolling_mean + (rolling_std * num_of_std)
  df['Bollinger Low'] = rolling_mean - (rolling_std * num_of_std)
  return df

data: pd.DataFrame = yf.download(STOCK, start="2020-01-01", end="2023-01-01")
bdata: pd.DataFrame = get_bollinger_bands(data)

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html ( make many subplots in one figure )
fig, a = plt.subplots()
a.plot(data['Close'], label='Close')
a.plot(bdata['Bollinger High'], label='Bollinger High')
a.plot(bdata['Bollinger Low'], label='Bollinger Low')
a.set_xlabel('Date')
a.set_ylabel('Price')
a.set_title(f'{STOCK} Bollinger Bands')
a.legend()
plt.show()
