'''
import tkinter as tk

root = tk.Tk()

root.geometry("800x500")

root.mainloop()
'''


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



import tkinter as tk
import yfinance as yf
import pandas as pd

def fetch_stock_data():
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

        data.append([ticker, rounded_open, rounded_high, rounded_low, rounded_close, volume])

    columns = ['Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = pd.DataFrame(data, columns=columns)

    return df

def create_table(parent, df):
    num_rows, num_cols = df.shape

    text_widget = tk.Text(parent, height=num_rows+1, width=50)
    text_widget.grid(row=0, column=0, padx=10, pady=10)

    # Insert column headers
    header = "\t".join(df.columns)
    text_widget.insert(tk.END, header + "\n")

    for i in range(num_rows):
        row = "\t".join(str(value) for value in df.iloc[i])
        text_widget.insert(tk.END, row + "\n")

def display_stock_data():
    df = fetch_stock_data()

    root = tk.Tk()
    root.title('Stock Data')

    create_table(root, df)

    root.mainloop()

display_stock_data()

