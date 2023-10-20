####
## Make the plot of comparison of two-five stocks. Daily chart for the year. Apple, Amazon Price charts. If requires normalization/rescale
####

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, Dict

def get_stock_hist(symbol: str, years: int = None) -> pd.DataFrame:
  if not years:
    years = 1
  stock = yf.Ticker(symbol)
  return stock.history(period=f"{years}y")

SELECTED_STOCKS: Tuple[str] = ("AAPL", "AMZN")

_output: Dict[str, pd.DataFrame] = {
  stock: get_stock_hist(stock)["Close"]
   for stock in SELECTED_STOCKS
}

# for stock in SELECTED_STOCKS:
#   data = get_stock_hist(stock)
#   _output[stock] = data['Close']

comparison_df: pd.DataFrame = pd.DataFrame(_output)

# Plot
plt.figure(figsize=(15, 6))
for stock in SELECTED_STOCKS:
  plt.plot(comparison_df.index, comparison_df[stock], label=stock)

plt.title(f'{", ".join(SELECTED_STOCKS)} Price Comparison (Past year)')
plt.xlabel('Date')
plt.ylabel('$Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
