import ta
import yfinance as yf
from matplotlib import pyplot as plt
from typing import Final

STOCK: Final[str] = "AAPL"

data = yf.download(STOCK, "2020-01-01", "2023-01-01")

closing_prices = data["Adj Close"]

rsi = ta.momentum.RSIIndicator(closing_prices, window=14)
rsi = rsi.rsi()

plt.plot(rsi, label="RSI")
plt.legend()
plt.show()

