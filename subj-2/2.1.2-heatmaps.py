###
## Use heat maps to visualize correlation coefficients between different stocks.
###
import pandas as pd
import yfinance as yf
import seaborn as sns # https://seaborn.pydata.org/
import matplotlib.pyplot as plt
from typing import Tuple

# STOCKS: Tuple[str] = ('META', 'AAPL', 'AMZN', 'NFLX', 'GOOG')

STOCKS: Tuple[str] = ("AAPL", "AMZN", "GOOGL", "MSFT", "TSLA")

data: pd.DataFrame = yf.download(STOCKS, start='2023-01-01', end='2023-10-07', group_by='ticker')

closing_prices: pd.DataFrame = pd.DataFrame()
for stock in STOCKS:
  closing_prices[stock] = data[stock]['Close']

plt.figure(figsize=(8, 6))
# .corr() => Correlation "matrix", annot => show num, cmap => color map, linewidths => line width (between boxes)
# spectral, coolwarm, magma, inferno, viridis, plasma, cividis
sns.heatmap(closing_prices.corr(), annot=True, cmap='coolwarm', linewidths=0.75)
plt.title('Correlation Coefficients Between Different Stocks')
plt.show()
