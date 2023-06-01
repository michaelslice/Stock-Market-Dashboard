'''
# GOOD CODE THAT PRINTS EVEN
import tkinter as tk    
from tkinter import ttk
import yfinance as yf
import os
from tkinter import messagebox

import stockprices
import stockcharts
import screener
import options
import company

def display_stock_prices():
    stockprices.display_stock_prices(window)
    
def display_screener():
    screener.display_screener(window)

def display_stock_charts():
    stockcharts.display_stock_charts(window)

def display_company_data():
    company.display_company_data(window)

def display_option_prices():
    options.display_option_prices(window)

# Function to open the settings file
def open_settings_file():
    # Open the settings file
    os.system("settings.py")  
    

def add_stock():
    stocks_input = entry_stock.get()  # Get the input stocks
    entry_stock.delete(0, tk.END)  # Clear the entry field

    if stocks_input:
        stocks_list = stocks_input.upper().split()  # Split the input stocks into a list

        for symbol in stocks_list:
            symbol = symbol[:4]  # Limit to maximum 4 characters

            if symbol in [child.cget("text") for child in stock_frame.winfo_children() if isinstance(child, ttk.Label)]:
                continue  # Skip adding repeated stocks

            # Check if the stock symbol is valid
            stock = yf.Ticker(symbol)
            if not stock.info:
                messagebox.showerror("Error", "Invalid stock symbol: " + symbol)
                continue

            row_index = len(stock_frame.grid_slaves())  # Get the row index for the new entry

            stock_name_label = ttk.Label(stock_frame, text=symbol)
            stock_name_label.grid(row=row_index, column=0, padx=5)

            remove_button = ttk.Button(stock_frame, text="Remove", command=lambda sym=symbol, row=row_index: remove_stock_details(sym, row_index))
            remove_button.grid(row=row_index, column=1, padx=5)

            details_button = ttk.Button(stock_frame, text="Details")
            details_button.grid(row=row_index, column=2, padx=5)


def remove_stock_details(symbol, row):
    # Remove stock name, details button, and remove button for the specified row
    for child in stock_frame.grid_slaves():
        if child.grid_info()["row"] == row:
            child.grid_forget()


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
button_settings = ttk.Button(window, text="!", command=open_settings_file)
button_save = ttk.Button(window, text="*", command=open_settings_file)

# Assign buttons to the same sizing group
window.grid_columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="equal")

# Place buttons in the window using grid layout
button_stock_prices.grid(row=0, column=0, padx=10, pady=10, sticky="we")
button_screener.grid(row=0, column=1, padx=10, pady=10, sticky="we")
button_stock_charts.grid(row=0, column=2, padx=10, pady=10, sticky="we")
button_company_data.grid(row=0, column=3, padx=10, pady=10, sticky="we")
button_option_prices.grid(row=0, column=4, padx=10, pady=10, sticky="we")
button_settings.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10, width=30, height=30)
button_save.place(relx=1.0, rely=1.0, anchor='se', x=-40, y=-10, width=30, height=30)

# Create a frame to hold the input elements
input_frame = ttk.Frame(window)
input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

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
label_output.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="w")

# Create a label to display the output
label_output = ttk.Label(window, wraplength=500)
label_output.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="w")

window.mainloop()
'''

# GOOD CODE THAT PRINTS EVEN
import tkinter as tk    
from tkinter import ttk
import yfinance as yf
import os
from tkinter import messagebox
# Database file path
DB_FILE = "data.db"

import stockprices
import stockcharts
import screener
import options
import company

def display_stock_prices():
    stockprices.display_stock_prices(window)
    
def display_screener():
    screener.display_screener(window)

def display_stock_charts():
    stockcharts.display_stock_charts(window)

def display_company_data():
    company.display_company_data(window)

def display_option_prices():
    options.display_option_prices(window)

# Function to open the settings file
def open_settings_file():
    # Open the settings file
    os.system("settings.py")  
    

def add_stock():
    stocks_input = entry_stock.get()  # Get the input stocks
    entry_stock.delete(0, tk.END)  # Clear the entry field

    if stocks_input:
        stocks_list = stocks_input.upper().split()  # Split the input stocks into a list

        for symbol in stocks_list:
            symbol = symbol[:4]  # Limit to maximum 4 characters

            if symbol in [child.cget("text") for child in stock_frame.winfo_children() if isinstance(child, ttk.Label)]:
                continue  # Skip adding repeated stocks

            # Check if the stock symbol is valid
            stock = yf.Ticker(symbol)
            if not stock.info:
                messagebox.showerror("Error", "Invalid stock symbol: " + symbol)
                continue

            row_index = len(stock_frame.grid_slaves())  # Get the row index for the new entry

            stock_name_label = ttk.Label(stock_frame, text=symbol)
            stock_name_label.grid(row=row_index, column=0, padx=5)

            remove_button = ttk.Button(stock_frame, text="Remove", command=lambda sym=symbol, row=row_index: remove_stock_details(sym, row_index))
            remove_button.grid(row=row_index, column=1, padx=5)

            details_button = ttk.Button(stock_frame, text="Details")
            details_button.grid(row=row_index, column=2, padx=5)


def remove_stock_details(symbol, row):
    # Remove stock name, details button, and remove button for the specified row
    for child in stock_frame.grid_slaves():
        if child.grid_info()["row"] == row:
            child.grid_forget()


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
button_settings = ttk.Button(window, text="!", command=open_settings_file)
button_save = ttk.Button(window, text="*", command=open_settings_file)

# Assign buttons to the same sizing group
window.grid_columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="equal")

# Place buttons in the window using grid layout
button_stock_prices.grid(row=0, column=0, padx=10, pady=10, sticky="we")
button_screener.grid(row=0, column=1, padx=10, pady=10, sticky="we")
button_stock_charts.grid(row=0, column=2, padx=10, pady=10, sticky="we")
button_company_data.grid(row=0, column=3, padx=10, pady=10, sticky="we")
button_option_prices.grid(row=0, column=4, padx=10, pady=10, sticky="we")
button_settings.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10, width=30, height=30)
button_save.place(relx=1.0, rely=1.0, anchor='se', x=-40, y=-10, width=30, height=30)

# Create a frame to hold the input elements
input_frame = ttk.Frame(window)
input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

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
label_output.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="w")

# Create a label to display the output
label_output = ttk.Label(window, wraplength=500)
label_output.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="w")

window.mainloop()