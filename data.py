import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

symbols = [
    "RELIANCE.NS", "HDFCBANK.NS", "INFY.NS", "TCS.NS", "ICICIBANK.NS",
    "SBIN.NS", "KOTAKBANK.NS", "HINDUNILVR.NS", "LT.NS", "AXISBANK.NS",
    "ITC.NS", "BAJFINANCE.NS", "ASIANPAINT.NS", "HCLTECH.NS", "WIPRO.NS",
    "MARUTI.NS", "ULTRACEMCO.NS", "NESTLEIND.NS", "TITAN.NS", "SUNPHARMA.NS",
    "POWERGRID.NS", "COALINDIA.NS", "ONGC.NS", "JSWSTEEL.NS", "TECHM.NS"
]

end_date = datetime.today()
start_date = end_date - timedelta(days=730)

os.makedirs("StockData", exist_ok=True)

for symbol in symbols:
    try:
        print(f"Downloading {symbol} ...")
        df = yf.download(symbol, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'), interval='1d')
        df.to_csv(f"StockData/{symbol.replace('.NS', '')}.csv")
    except Exception as e:
        print(f"Failed to download {symbol}: {e}")

print("Data Fetched")
