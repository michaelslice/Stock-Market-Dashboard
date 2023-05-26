import tkinter as tk
from tkinter import ttk
import yfinance as yf
import os

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

# Function to open the settings file
def open_settings_file():
    # Open the settings file
    os.system("settings.py")  # Replace "notepad.exe" with the appropriate program for your file type

def add_stock():
    symbol = entry_stock.get().upper()[:4]  # Limit to maximum 4 characters
    entry_stock.delete(0, tk.END)  # Clear the entry field

    if symbol:
        # Check if the stock is already present in the stock list
        stocks = [child.winfo_children()[0].cget("text") for child in stock_frame.winfo_children()]
        if symbol in stocks:
            return  # Do not add repeated stocks

        # Create a new frame for the stock entry
        stock_entry_frame = ttk.Frame(stock_frame)
        stock_entry_frame.pack(side=tk.TOP, pady=5)

        # Create a label for the stock name
        stock_name_label = ttk.Label(stock_entry_frame, text=symbol)
        stock_name_label.pack(side=tk.LEFT)

        # Create the "Remove" button
        remove_button = ttk.Button(stock_entry_frame, text="Remove", command=lambda: remove_stock(stock_entry_frame))
        remove_button.pack(side=tk.LEFT, padx=5)

        # Create the "Details" button
        details_button = ttk.Button(stock_entry_frame, text="Details")
        details_button.pack(side=tk.LEFT, padx=5)

        # Set the column to zero for all widgets in stock_entry_frame
        for child in stock_entry_frame.winfo_children():
            child.pack(side=tk.LEFT)

        # Increment the row index for the next stock entry
        stock_frame.grid_rowconfigure(stock_frame.grid_size()[1] + 1, weight=1)

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
button_settings = ttk.Button(window, text="!", command=open_settings_file)

# Assign buttons to the same sizing group
window.grid_columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="equal")

# Place buttons in the window using grid layout
button_stock_prices.grid(row=0, column=0, padx=10, pady=10, sticky="we")
button_option_prices.grid(row=0, column=1, padx=10, pady=10, sticky="we")
button_screener.grid(row=0, column=2, padx=10, pady=10, sticky="we")
button_company_data.grid(row=0, column=3, padx=10, pady=10, sticky="we")
button_stock_charts.grid(row=0, column=4, padx=10, pady=10, sticky="we")
button_settings.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10, width=30, height=30)

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