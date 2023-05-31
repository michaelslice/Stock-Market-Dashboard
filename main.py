
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


from yahoo_fin import stock_info as si
from yahoo_fin import stock_info as si
from yahoo_fin import stock_info as si
import yfinance as yf

import yfinance as yf

# CREATE A TICKER INSTANCE PASSING TESLA AS THE TARGET COMPANY
tsla = yf.Ticker('TSLA')

# CALL THE MULTIPLE FUNCTIONS AVAILABLE AND STORE THEM IN VARIABLES.
actions = tsla.get_actions()
analysis = tsla.get_analysis()
balance = tsla.get_balance_sheet()
calendar = tsla.get_calendar()
cf = tsla.get_cashflow()
info = tsla.get_info()
inst_holders = tsla.get_institutional_holders()
news = tsla.get_news()
recommendations = tsla.get_recommendations()
sustainability = tsla.get_sustainability()

# PRINT THE RESULTS
print(actions)
print('*'*20)
print(analysis)
print('*'*20)
print(balance)
print('*'*20)
print(calendar)
print('*'*20)
print(cf)
print('*'*20)
print(info)
print('*'*20)
print(inst_holders)
print('*'*20)
print(news)
print('*'*20)
print(recommendations)
print('*'*20)
print(sustainability)
print('*'*20)


# IMPORT REQUIRED LIBRARY
import yfinance as yf

# CREATE A TICKER INSTANCE FOR TESLA
tsla = yf.Ticker('TSLA')

# FETCH OPTIONS CHAIN DATA FOR THE COMPANY
tsla_options = tsla.option_chain()

# ACCESS BOTH THE CALLS AND PUTS AND STORE THEM IN THEIR RESPECTIVE VARIABLES
tsla_puts = tsla_options.puts
tsla_calls = tsla_options.calls