###
## Make a table of stocks for five stocks (similar to above). At this time, show the probability of being a positive change for the next day if two consecutive days are positive. Do this for three, four, five, and six consecutive days.						
###

import yfinance as yf, matplotlib.pyplot as plt, pandas as pd
from typing import Tuple

# Function to fetch historical stock data
def get_stock_hist(symbol, years=2) -> pd.DataFrame:
  stock = yf.Ticker(symbol)
  return stock.history(period=f"{years}y")
 
STOCKS: Tuple[str] = ('META', 'AMZN', 'NFLX', 'GOOGL', 'AAPL') 
# Days to analyze (2, 3, 4, 5, 6)
CONSEC_DAYS: Tuple[int] = (2, 3, 4, 5, 6)

results = pd.DataFrame(columns=CONSEC_DAYS)

for stock in STOCKS:
  data = get_stock_hist(stock)
  price_changes = data['Close'].pct_change() > 0
  print("AAA", price_changes)
  probabilities = []
  for days in CONSEC_DAYS: # 2, 3, 4, 5, 6
    # .rolling() creates a window of the specified size, them we use .sum() to count the number of True values
    # Calculate if there were 'days' consecutive positive changes in stock prices
    consecutive_positive = price_changes.rolling(window=days).sum() == days 
    # probably = (numb of positive) / (total days) * 100
    probability = (consecutive_positive.sum() / len(consecutive_positive)) * 100 # multiply by 100 to get real percentage 0.5 = 50%
    probabilities.append(probability)

  results.loc[stock] = probabilities


# plot data
plt.figure(figsize=(12, 6))
for stock in STOCKS:
  plt.plot(CONSEC_DAYS, results.T[stock], label=stock)

plt.title("Probability of Positive Change for Consec Days Positive")
plt.xlabel("Consecutive Days")
plt.ylabel("Probability (%)")
plt.xticks(CONSEC_DAYS)
plt.legend()
plt.grid(True)
plt.show()
