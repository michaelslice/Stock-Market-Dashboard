import tkinter as tk    
from tkinter import ttk
import yfinance as yf
import os
from tkinter import messagebox
import sqlite3

import stockprices
import stockcharts
import screener
import options
import company
import settings

DB_FILE = "data.db"
 
# Create a connection to the SQLite database
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

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

def open_settings_window():
    settings.open_settings_window

# Function to open the settings file
def open_settings_file():
    # Reset the database
    cursor.execute("DROP TABLE IF EXISTS stocks")
    cursor.execute("CREATE TABLE stocks (symbol TEXT)")

    # Clear the displayed stocks on the screen
    for child in stock_frame.grid_slaves():
        child.grid_forget()

    # Reload the stocks from the database (which will be empty after reset)
    load_stocks()

    # Show a message box to indicate successful reset
    messagebox.showinfo("Reset", "The database and displayed stocks have been reset.")
 
    
def add_stock():
    stocks_input = entry_stock.get().strip().upper()  # Get the input stocks
    entry_stock.delete(0, tk.END)  # Clear the entry field

    if stocks_input:
        stocks_list = stocks_input.split()  # Split the input stocks into a list

        for symbol in stocks_list:
            symbol = symbol[:4]  # Limit to maximum 4 characters

            # Check if the stock symbol is already displayed on the screen
            for child in stock_frame.grid_slaves():
                if isinstance(child, ttk.Label) and child.cget("text") == symbol:
                    messagebox.showerror("Error", "Stock symbol already displayed: " + symbol)
                    break
            else:
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

                details_button = ttk.Button(stock_frame, text="Details", command=lambda sym=symbol: display_historical_data(sym))
                details_button.grid(row=row_index, column=2, padx=5)

                # Insert the stock symbol into the database
                cursor.execute("INSERT INTO stocks (symbol) VALUES (?)", (symbol,))
                conn.commit()

        # Reload the stocks from the database
        load_stocks()



def remove_stock_details(symbol, row):
    # Remove stock name, details button, and remove button for the specified row
    for child in stock_frame.grid_slaves():
        if child.grid_info()["row"] == row:
            child.grid_forget()
            
    # Delete the stock from the database
    cursor.execute("DELETE FROM stocks WHERE symbol=?", (symbol,))
    conn.commit()

def load_stocks():
    # Clear the displayed stocks on the screen
    for child in stock_frame.grid_slaves():
        child.grid_forget()

    # Retrieve the stocks from the database
    cursor.execute("SELECT symbol FROM stocks")
    stocks = cursor.fetchall()

    displayed_stocks = set()  # Track the displayed stocks

    for row_index, stock in enumerate(stocks):
        symbol = stock[0]
        
        # Check if the stock is already displayed
        if symbol in displayed_stocks:
            continue

        stock_name_label = ttk.Label(stock_frame, text=symbol)
        stock_name_label.grid(row=row_index, column=0, padx=5)

        remove_button = ttk.Button(stock_frame, text="Remove", command=lambda sym=symbol, row=row_index: remove_stock_details(sym, row_index))
        remove_button.grid(row=row_index, column=1, padx=5)

        details_button = ttk.Button(stock_frame, text="Details", command=lambda sym=symbol: display_historical_data(sym))
        details_button.grid(row=row_index, column=2, padx=5)

        displayed_stocks.add(symbol)  # Add the stock to the displayed stocks set



# Create the main window
window = tk.Tk()
window.title("Stock Tracker")


# Create buttons
button_stock_prices = ttk.Button(window, text="Sectors", command=display_stock_prices)
button_option_prices = ttk.Button(window, text="Option Prices", command=display_option_prices)
button_screener = ttk.Button(window, text="Screener", command=display_screener)
button_company_data = ttk.Button(window, text="Company Data", command=display_company_data)
button_stock_charts = ttk.Button(window, text="Stock Charts", command=display_stock_charts)
button_settings = ttk.Button(window, text="!", command=open_settings_file)
button_save = ttk.Button(window, text="*", command=open_settings_window)

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

# Create the ButtonFunctions instance
button_functions = settings.ButtonFunctions(window)

# Assign the open_settings_window method as the command for the "*" button
button_save.config(command=button_functions.open_settings_window)

# Create a frame to hold the input elements
input_frame = ttk.Frame(window)
input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Create a StringVar variable for the entry field
entry_var = tk.StringVar()

# Create entry field to enter stock symbols
entry_stock = ttk.Entry(input_frame, width=15, textvariable=entry_var)  # Adjust the width as needed
entry_stock.pack(padx=10, pady=10)

# Function to validate the input and convert it to uppercase
def validate_input(*args):
    entry_var.set(entry_var.get().upper())  # Convert the input to uppercase
    if entry_var.get().strip():
        button_add_stock.config(state=tk.NORMAL)
    else:
        button_add_stock.config(state=tk.DISABLED)

entry_var.trace("w", validate_input)  # Bind the validation function to the entry variable

# Create button to add stocks
button_add_stock = ttk.Button(input_frame, text="Add Stock", command=add_stock, width=15, state=tk.DISABLED)  # Adjust the width as needed
button_add_stock.pack(padx=10, pady=10)

# Create a frame to hold stock data labels
stock_frame = ttk.Frame(window)
stock_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Create a label to display the output
label_output = ttk.Label(window, wraplength=500)
label_output.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="w")

# Create a label to display the output
label_output = ttk.Label(window, wraplength=500)
label_output.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="w")

load_stocks()

def display_historical_data(symbol):
    # Create a new window for displaying historical data
    historical_window = tk.Toplevel(window)
    historical_window.title("Historical Data: " + symbol)

    # Retrieve the historical data for the stock using yfinance or any other library
    # Customize the code below according to your specific data retrieval and display needs
    stock = yf.Ticker(symbol)
    historical_data = stock.history(period="max")

    historical_data = historical_data.sort_index(ascending=False)

    frame = ttk.Frame(historical_window, padding=(10, 0, 10, 0))
    frame.pack(fill=tk.BOTH, expand=True)

    tree = ttk.Treeview(frame)
    tree.pack(fill=tk.BOTH, expand=True, padx=10)  

    tree["columns"] = ("Date", "Open", "High", "Low", "Close", "Volume")
    tree.column("#0", width=0, stretch=tk.NO)  

    tree.heading("Date", text="Date")
    tree.heading("Open", text="Open")
    tree.heading("High", text="High")
    tree.heading("Low", text="Low")
    tree.heading("Close", text="Close")
    tree.heading("Volume", text="Volume")

    for row in historical_data.itertuples():
        date = row.Index.strftime("%m/%d/%Y")  
        values = row[1:]
        # Round the values in the "Open", "High", "Low", and "Close" columns to the nearest hundredth
        rounded_values = [round(value, 2) if isinstance(value, (int, float)) else value for value in values[:4]]
        tree.insert("", tk.END, values=(date,) + tuple(rounded_values) + values[4:])

    scrollbar = ttk.Scrollbar(historical_window, orient=tk.VERTICAL, command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.configure(yscrollcommand=scrollbar.set)

window.mainloop()