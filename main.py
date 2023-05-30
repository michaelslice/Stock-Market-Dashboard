
'''



import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'META', 'TSLA', 'V', 'UNH',
           'XOM', 'JNJ', 'LLY', 'WMT', 'JPM', 'MA', 'PG', 'HD', 'CVX', 'MRK', 'AVGO',
           'ORCL', 'KO', 'PEP', 'ABBV', 'BAC', 'PFE', 'COST', 'MCD', 'CRM', 'TMO',
           'CSCO', 'ACN', 'ABT', 'AMD', 'LIN', 'ADBE', 'DHR', 'TMUS', 'CMCSA', 'NKE']

data = []

for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    temp_data = ticker_yahoo.history(period='1d')
    
    last_row = temp_data.iloc[-1]
    rounded_close = round(last_row['Close'], 2)
    rounded_open = round(last_row['Open'], 2)
    rounded_high = round(last_row['High'], 2)
    rounded_low = round(last_row['Low'], 2)
    volume = last_row['Volume']
    
    data.append([rounded_open, rounded_high, rounded_low, rounded_close, volume])

columns = ['Open', 'High', 'Low', 'Close', 'Volume']
df = pd.DataFrame(data, index=tickers, columns=columns)

print(df)

'''
''''''
import yfinance as yf
from yahoo_fin import options as ops


ticker = yf.Ticker("AAPL")

option_chain = ticker.option_chain('2023-06-16').calls

# Print the option quotes
print(option_chain.head())



ticker.options

print(ticker.options)



ops.get_calls("aapl")
ops.get_puts("aapl")


print(ops.get_puts("aapl"))



import yfinance as yf

msft = yf.Ticker("MSFT")




msft.cashflow
print(msft)