'''


import tkinter as tk
from tkinter import ttk
import yfinance as yf

class CompanyDataWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Option Prices")

        # Create a frame for the search input
        search_frame = ttk.Frame(self)
        search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        # Create and position the input box for search
        self.search_entry = ttk.Entry(search_frame, width=10)
        self.search_entry.grid(row=0, column=0, sticky="we")

        input_frame = ttk.Frame(self)
        input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Create a frame for the filter button
        self.button_add_stock = ttk.Button(input_frame, text="Add Stock", width=15, state=tk.DISABLED)
        self.button_add_stock.pack(pady=10)

        # Bind a function to the button click event
        self.button_add_stock.config(command=self.get_stock_data)

        # Create labels for 52-week high and low
        self.high_label = ttk.Label(self, text="52-Week High: ")
        self.low_label = ttk.Label(self, text="52-Week Low: ")
        self.high_label.grid(row=0, column=1, sticky="ne")
        self.low_label.grid(row=1, column=1, sticky="ne")

        self.stock_symbol = ""

        # Bind the Enter key to the search entry
        self.search_entry.bind('<Return>', self.add_stock_button_click)
        self.search_entry.bind('<KeyRelease>', self.check_input_validity)

        # Create a label widget for displaying dividend data
        self.dividend_label = ttk.Label(self)
        self.dividend_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    def add_stock_button_click(self, event):
        self.get_stock_data()

    def check_input_validity(self, event):
        symbol = self.search_entry.get()
        if symbol:
            self.button_add_stock.config(state=tk.NORMAL)
        else:
            self.button_add_stock.config(state=tk.DISABLED)

    def get_stock_data(self):
        symbol = self.search_entry.get()
        stock = yf.Ticker(symbol)
        info = stock.info
        if 'fiftyTwoWeekHigh' in info and 'fiftyTwoWeekLow' in info:
            high = info['fiftyTwoWeekHigh']
            low = info['fiftyTwoWeekLow']
            self.high_label.config(text=f"52-Week High: {high}")
            self.low_label.config(text=f"52-Week Low: {low}")
        else:
            self.high_label.config(text="52-Week High: N/A")
            self.low_label.config(text="52-Week Low: N/A")

        # Clear the existing dividend data
        self.dividend_label.config(text="")

        # Fetch dividend data
        dividends = stock.dividends
        if dividends.empty:
            self.dividend_label.config(text="No dividend data available.")
        else:
            dividend_data = "Dividends: "
            for date, dividend in dividends.tail(3).items():
                formatted_date = date.strftime("%Y/%m/%d")
                dividend_info = f"{formatted_date}: ${dividend} | "
                dividend_data += dividend_info

            # Remove the last "| " from the dividend_data
            dividend_data = dividend_data.rstrip("| ")

            # Create a label for dividend data
            dividend_label = ttk.Label(self, text=dividend_data)
            dividend_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

def display_company_data(parent):
    option_window = CompanyDataWindow(parent)

   '''


import tkinter as tk
from tkinter import ttk
import yfinance as yf

class CompanyDataWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Option Prices")

        # Create a frame for the search input
        search_frame = ttk.Frame(self)
        search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        # Create and position the input box for search
        self.search_entry = ttk.Entry(search_frame, width=10)
        self.search_entry.grid(row=0, column=0, sticky="we")

        input_frame = ttk.Frame(self)
        input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Create a frame for the filter button
        self.button_add_stock = ttk.Button(input_frame, text="Add Stock", width=15, state=tk.DISABLED)
        self.button_add_stock.pack(pady=10)

        # Bind a function to the button click event
        self.button_add_stock.config(command=self.get_stock_data)

        # Create labels for 52-week high and low
        self.high_label = ttk.Label(self, text="52-Week High: ")
        self.low_label = ttk.Label(self, text="52-Week Low: ")
        self.high_label.grid(row=0, column=1, sticky="ne")
        self.low_label.grid(row=1, column=1, sticky="ne")

        self.stock_symbol = ""

        # Bind the Enter key to the search entry
        self.search_entry.bind('<Return>', self.add_stock_button_click)
        self.search_entry.bind('<KeyRelease>', self.check_input_validity)

        # Create a label widget for displaying dividend data
        self.dividend_label = ttk.Label(self)
        self.dividend_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    def add_stock_button_click(self, event):
        self.get_stock_data()

    def check_input_validity(self, event):
        symbol = self.search_entry.get()
        if symbol:
            self.button_add_stock.config(state=tk.NORMAL)
        else:
            self.button_add_stock.config(state=tk.DISABLED)

    def get_stock_data(self):
        symbol = self.search_entry.get()
        stock = yf.Ticker(symbol)
        info = stock.info
        if 'fiftyTwoWeekHigh' in info and 'fiftyTwoWeekLow' in info:
            high = info['fiftyTwoWeekHigh']
            low = info['fiftyTwoWeekLow']
            self.high_label.config(text=f"52-Week High: {high}")
            self.low_label.config(text=f"52-Week Low: {low}")
        else:
            self.high_label.config(text="52-Week High: N/A")
            self.low_label.config(text="52-Week Low: N/A")

        # Clear the existing dividend data
        self.dividend_label.config(text="")

        # Fetch dividend data
        dividends = stock.dividends
        if dividends.empty:
            self.dividend_label.config(text="No dividend data available.")
        else:
            dividend_data = "Dividends: "
            for date, dividend in dividends.tail(3).items():
                formatted_date = date.strftime("%Y/%m/%d")
                dividend_info = f"{formatted_date}: ${dividend} | "
                dividend_data += dividend_info

            # Remove the last "| " from the dividend_data
            dividend_data = dividend_data.rstrip("| ")

            # Create a label for dividend data
            dividend_label = ttk.Label(self, text=dividend_data)
            dividend_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

def display_company_data(parent):
    option_window = CompanyDataWindow(parent)