import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf

STOCK: str = "NVDA"

data = yf.download(STOCK, start="2020-01-01", end="2023-01-01")

mpf.plot(data, type="candle", title=f"{STOCK} Candlestick Chart")
plt.show()
