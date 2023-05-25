
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
    symbol = entry_stock.get().upper()
    entry_stock.delete(0, tk.END)  # Clear the entry field

    # Create a new label for the stock name
    stock_name_label = ttk.Label(stock_frame, text=symbol)
    stock_name_label.pack(side=tk.TOP, pady=5)

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
button_add_stock = ttk.Button(input_frame, text="Add Stock", command=add_stock, width=15)  # Adjust the width as needed
button_add_stock.pack(padx=10, pady=10)

# Create a frame to hold stock data labels
stock_frame = ttk.Frame(window)
stock_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Create a label to display the output
label_output = ttk.Label(window, wraplength=500)
label_output.grid(row=3, column=0, columnspan=5, padx=10, pady=10, sticky="w")

window.mainloop()