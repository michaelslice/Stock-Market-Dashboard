'''
#DECENT CODE THAT PRINTS THE STOCK NAME AND THE FINANCIALS FOR IT


import tkinter as tk
from tkinter import ttk
import yfinance as yf

def display_stock_prices():
    output = "Displaying stock prices..."
    label_output.config(text=output)

def display_option_prices():
    output = "Displaying option prices..."
    label_output.config(text=output)

def display_screener():
    output = "Displaying screener..."
    label_output.config(text=output)

def display_company_data():
    output = "Displaying company data..."
    label_output.config(text=output)

def display_stock_charts():
    output = "Displaying stock charts..."
    label_output.config(text=output)

def add_stock():
    symbol = entry_stock.get().upper()[:4]  # Limit to maximum 4 characters
    entry_stock.delete(0, tk.END)  # Clear the entry field

    if symbol:
        # Check if the stock is already present in the stock list
        stocks = [child.winfo_children()[0].cget("text") for child in stock_frame.winfo_children()]
        if symbol in stocks:
            return  # Do not add repeated stocks

        # Create a new frame for the stock information
        stock_entry_frame = ttk.Frame(stock_frame)
        stock_entry_frame.pack(side=tk.TOP, pady=5)

        # Retrieve stock information using yfinance
        stock_data = yf.download(symbol, period='1d', start='2023-05-25', end='2023-05-25')

        # Extract relevant data from the stock data
        stock_open = stock_data['Open'][0]
        stock_high = stock_data['High'][0]
        stock_low = stock_data['Low'][0]
        stock_close = stock_data['Close'][0]
        stock_volume = stock_data['Volume'][0]

        # Create labels for the stock information
        stock_name_label = ttk.Label(stock_entry_frame, text=symbol)
        stock_name_label.pack(side=tk.LEFT)

        stock_open_label = ttk.Label(stock_entry_frame, text=f"Open: {stock_open:.2f}")
        stock_open_label.pack(side=tk.LEFT)

        stock_high_label = ttk.Label(stock_entry_frame, text=f"High: {stock_high:.2f}")
        stock_high_label.pack(side=tk.LEFT)

        stock_low_label = ttk.Label(stock_entry_frame, text=f"Low: {stock_low:.2f}")
        stock_low_label.pack(side=tk.LEFT)

        stock_close_label = ttk.Label(stock_entry_frame, text=f"Close: {stock_close:.2f}")
        stock_close_label.pack(side=tk.LEFT)

        stock_volume_label = ttk.Label(stock_entry_frame, text=f"Volume: {stock_volume}")
        stock_volume_label.pack(side=tk.LEFT)

        remove_button = ttk.Button(stock_entry_frame, text="Remove", command=lambda: remove_stock(stock_entry_frame))
        remove_button.pack(side=tk.LEFT, padx=5)

def remove_stock(stock_entry_frame):
    stock_entry_frame.destroy()

def validate_input(*args):
    if entry_stock.get().strip():
        button_add_stock.config(state=tk.NORMAL)
    else:
        button_add_stock.config(state=tk.DISABLED)

# Create the main window
window = tk.Tk()
window.title("Stock Tracker")

# Create buttons
button_stock_prices = ttk.Button(window, text="Stock Prices", command=display_stock_prices)
button_option_prices = ttk.Button(window, text="Option Prices", command=display_option_prices)
button_screener = ttk.Button(window, text="Screener", command=display_screener)
button_company_data = ttk.Button(window, text="Company Data", command=display_company_data)
button_stock_charts = ttk.Button(window, text="Stock Charts", command=display_stock_charts)

# Place buttons in the window using grid layout
button_stock_prices.grid(row=0, column=0, padx=10, pady=10)
button_option_prices.grid(row=0, column=1, padx=10, pady=10)
button_screener.grid(row=0, column=2, padx=10, pady=10)
button_company_data.grid(row=0, column=3, padx=10, pady=10)
button_stock_charts.grid(row=0, column=4, padx=10, pady=10)

# Create a frame to hold the input elements
input_frame = ttk.Frame(window)
input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Create entry field to enter stock symbols
entry_stock = ttk.Entry(input_frame, width=15)  # Adjust the width as needed
entry_stock.pack(padx=10, pady=10)

# Create button to add stocks
button_add_stock = ttk.Button(input_frame, text="Add Stock", command=add_stock, width=15, state=tk.DISABLED)  # Adjust the width as needed
button_add_stock.pack(padx=10, pady=10)

entry_stock.bind("<KeyRelease>", validate_input)  # Bind the validation function to the entry field

# Create a frame to hold stock data labels
stock_frame = ttk.Frame(window)
stock_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Create a label to display the output
label_output = ttk.Label(window, wraplength=500)
label_output.grid(row=3, column=0, columnspan=5, padx=10, pady=10, sticky="w")

window.mainloop()

'''

'''

#code that prints ok

import tkinter as tk
from tkinter import ttk
import yfinance as yf

def display_stock_prices():
    output = "Displaying stock prices..."
    label_output.config(text=output)

def display_option_prices():
    output = "Displaying option prices..."
    label_output.config(text=output)

def display_screener():
    output = "Displaying screener..."
    label_output.config(text=output)

def display_company_data():
    output = "Displaying company data..."
    label_output.config(text=output)

def display_stock_charts():
    output = "Displaying stock charts..."
    label_output.config(text=output)

def add_stock():
    symbol = entry_stock.get().upper()[:4]  # Limit to maximum 4 characters
    entry_stock.delete(0, tk.END)  # Clear the entry field

    if symbol:
        # Check if the stock is already present in the stock list
        stocks = [child.winfo_children()[0].cget("text") for child in stock_frame.winfo_children()]
        if symbol in stocks:
            return  # Do not add repeated stocks

        # Create a new frame for the stock information
        stock_entry_frame = ttk.Frame(stock_frame)
        stock_entry_frame.pack(side=tk.TOP, pady=5)

        # Retrieve stock information using yfinance
        stock_data = yf.download(symbol, period='1d', start='2023-05-25', end='2023-05-25')

        # Extract relevant data from the stock data
        stock_open = stock_data['Open'][0]
        stock_high = stock_data['High'][0]
        stock_low = stock_data['Low'][0]
        stock_close = stock_data['Close'][0]
        stock_volume = stock_data['Volume'][0]

        # Create a frame for the financial information
        financial_frame = ttk.Frame(stock_entry_frame)
        financial_frame.pack(side=tk.RIGHT)

        # Create labels for the stock information
        stock_name_label = ttk.Label(stock_entry_frame, text=symbol)
        stock_name_label.pack(side=tk.LEFT)

        remove_button = ttk.Button(stock_entry_frame, text="Remove", command=lambda: remove_stock(stock_entry_frame))
        remove_button.pack(side=tk.LEFT, padx=5)

        # Create labels for the financial information
        stock_open_label = ttk.Label(financial_frame, text=f"Open: {stock_open:.2f}")
        stock_open_label.pack(side=tk.LEFT, padx=5)

        stock_high_label = ttk.Label(financial_frame, text=f"High: {stock_high:.2f}")
        stock_high_label.pack(side=tk.LEFT, padx=5)

        stock_low_label = ttk.Label(financial_frame, text=f"Low: {stock_low:.2f}")
        stock_low_label.pack(side=tk.LEFT, padx=5)

        stock_close_label = ttk.Label(financial_frame, text=f"Close: {stock_close:.2f}")
        stock_close_label.pack(side=tk.LEFT, padx=5)

        stock_volume_label = ttk.Label(financial_frame, text=f"Volume: {stock_volume}")
        stock_volume_label.pack(side=tk.LEFT, padx=5)

def remove_stock(stock_entry_frame):
    stock_entry_frame.destroy()

def validate_input(*args):
    if entry_stock.get().strip():
        button_add_stock.config(state=tk.NORMAL)
    else:
        button_add_stock.config(state=tk.DISABLED)



# Create the main window
window = tk.Tk()
window.title("Stock Tracker")

# Create buttons
button_stock_prices = ttk.Button(window, text="Stock Prices", command=display_stock_prices)
button_option_prices = ttk.Button(window, text="Option Prices", command=display_option_prices)
button_screener = ttk.Button(window, text="Screener", command=display_screener)
button_company_data = ttk.Button(window, text="Company Data", command=display_company_data)
button_stock_charts = ttk.Button(window, text="Stock Charts", command=display_stock_charts)

# Place buttons in the window using grid layout
button_stock_prices.grid(row=0, column=0, padx=10, pady=10)
button_option_prices.grid(row=0, column=1, padx=10, pady=10)
button_screener.grid(row=0, column=2, padx=10, pady=10)
button_company_data.grid(row=0, column=3, padx=10, pady=10)
button_stock_charts.grid(row=0, column=4, padx=10, pady=10)

# Create a frame to hold the input elements
input_frame = ttk.Frame(window)
input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Create entry field to enter stock symbols
entry_stock = ttk.Entry(input_frame, width=15)  # Adjust the width as needed
entry_stock.pack(padx=10, pady=10)

# Create button to add stocks
button_add_stock = ttk.Button(input_frame, text="Add Stock", command=add_stock, width=15, state=tk.DISABLED)  # Adjust the width as needed
button_add_stock.pack(padx=10, pady=10)

entry_stock.bind("<KeyRelease>", validate_input)  # Bind the validation function to the entry field

# Create a frame to hold stock data labels
stock_frame = ttk.Frame(window)
stock_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Create a label to display the output
label_output = ttk.Label(window, wraplength=500)
label_output.grid(row=3, column=0, columnspan=5, padx=10, pady=10, sticky="w")

window.mainloop()


'''

import tkinter as tk
from tkinter import ttk
import yfinance as yf

def display_stock_prices():
    output = "Displaying stock prices..."
    label_output.config(text=output)

def display_option_prices():
    output = "Displaying option prices..."
    label_output.config(text=output)

def display_screener():
    output = "Displaying screener..."
    label_output.config(text=output)

def display_company_data():
    output = "Displaying company data..."
    label_output.config(text=output)

def display_stock_charts():
    output = "Displaying stock charts..."
    label_output.config(text=output)

def add_stock():
    symbol = entry_stock.get().upper()[:4]  # Limit to maximum 4 characters
    entry_stock.delete(0, tk.END)  # Clear the entry field

    if symbol:
        # Check if the stock is already present in the stock list
        stocks = [child.winfo_children()[0].cget("text") for child in stock_frame.winfo_children()]
        if symbol in stocks:
            return  # Do not add repeated stocks

        # Create a new frame for the stock information
        stock_entry_frame = ttk.Frame(stock_frame)
        stock_entry_frame.pack(side=tk.TOP, pady=5)

        # Retrieve stock information using yfinance
        stock_data = yf.download(symbol, period='1d', start='2023-05-25', end='2023-05-25')

        # Extract relevant data from the stock data
        stock_open = stock_data['Open'][0]
        stock_high = stock_data['High'][0]
        stock_low = stock_data['Low'][0]
        stock_close = stock_data['Close'][0]
        stock_volume = stock_data['Volume'][0]

        # Create a frame for the financial information
        financial_frame = ttk.Frame(stock_entry_frame)
        financial_frame.pack(side=tk.RIGHT)

        # Create labels for the stock information
        stock_name_label = ttk.Label(stock_entry_frame, text=symbol)
        stock_name_label.pack(side=tk.LEFT)

        remove_button = ttk.Button(stock_entry_frame, text="Remove", command=lambda: remove_stock(stock_entry_frame))
        remove_button.pack(side=tk.LEFT, padx=5)

        # Create labels for the financial information
        stock_open_label = ttk.Label(financial_frame, text=f"Open: {stock_open:.2f}")
        stock_open_label.pack(side=tk.LEFT, padx=5)

        stock_high_label = ttk.Label(financial_frame, text=f"High: {stock_high:.2f}")
        stock_high_label.pack(side=tk.LEFT, padx=5)

        stock_low_label = ttk.Label(financial_frame, text=f"Low: {stock_low:.2f}")
        stock_low_label.pack(side=tk.LEFT, padx=5)

        stock_close_label = ttk.Label(financial_frame, text=f"Close: {stock_close:.2f}")
        stock_close_label.pack(side=tk.LEFT, padx=5)

        stock_volume_label = ttk.Label(financial_frame, text=f"Volume: {stock_volume}")
        stock_volume_label.pack(side=tk.LEFT, padx=5)

def remove_stock(stock_entry_frame):
    stock_entry_frame.destroy()

def validate_input(*args):
    if entry_stock.get().strip():
        button_add_stock.config(state=tk.NORMAL)
    else:
        button_add_stock.config(state=tk.DISABLED)



# Create the main window
window = tk.Tk()
window.title("Stock Tracker")

# Create buttons
button_stock_prices = ttk.Button(window, text="Stock Prices", command=display_stock_prices)
button_option_prices = ttk.Button(window, text="Option Prices", command=display_option_prices)
button_screener = ttk.Button(window, text="Screener", command=display_screener)
button_company_data = ttk.Button(window, text="Company Data", command=display_company_data)
button_stock_charts = ttk.Button(window, text="Stock Charts", command=display_stock_charts)

# Place buttons in the window using grid layout
button_stock_prices.grid(row=0, column=0, padx=10, pady=10)
button_option_prices.grid(row=0, column=1, padx=10, pady=10)
button_screener.grid(row=0, column=2, padx=10, pady=10)
button_company_data.grid(row=0, column=3, padx=10, pady=10)
button_stock_charts.grid(row=0, column=4, padx=10, pady=10)

# Create a frame to hold the input elements
input_frame = ttk.Frame(window)
input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Create entry field to enter stock symbols
entry_stock = ttk.Entry(input_frame, width=15)  # Adjust the width as needed
entry_stock.pack(padx=10, pady=10)

# Create button to add stocks
button_add_stock = ttk.Button(input_frame, text="Add Stock", command=add_stock, width=15, state=tk.DISABLED)  # Adjust the width as needed
button_add_stock.pack(padx=10, pady=10)

entry_stock.bind("<KeyRelease>", validate_input)  # Bind the validation function to the entry field

# Create a frame to hold stock data labels
stock_frame = ttk.Frame(window)
stock_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Create a label to display the output
label_output = ttk.Label(window, wraplength=500)
label_output.grid(row=3, column=0, columnspan=5, padx=10, pady=10, sticky="w")

window.mainloop()




