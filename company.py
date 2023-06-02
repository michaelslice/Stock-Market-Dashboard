import tkinter as tk
from tkinter import ttk
import yfinance as yf
from yahoo_fin import stock_info as si

class CompanyDataWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Company Data")

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

        # Create a label widget for displaying stock splits data
        self.splits_label = ttk.Label(self)
        self.splits_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        # Create a label widget for displaying earnings dates
        self.earnings_label = ttk.Label(self)
        self.earnings_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    def add_stock_button_click(self, event):
        self.get_stock_data()

    def check_input_validity(self, event):
        symbol = self.search_entry.get().upper()  # Convert the input to uppercase
        self.search_entry.delete(0, tk.END)  # Clear the entry field
        self.search_entry.insert(0, symbol)  # Update the entry field with the uppercase input

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

        # Clear the existing stock splits data
        self.splits_label.config(text="")

        # Fetch stock splits data
        splits = stock.splits
        if splits.empty:
            self.splits_label.config(text="No stock splits data available.")
        else:
            splits_data = "Splits: "
            for date, split in splits.tail(3).items():
                formatted_date = date.strftime("%Y/%m/%d")
                split_info = f"{formatted_date}: {split} | "
                splits_data += split_info

            # Remove the last "| " from the splits_data
            splits_data = splits_data.rstrip("| ")

            # Create a label for stock splits data
            splits_label = ttk.Label(self, text=splits_data)
            splits_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

            # Fetch volume data for the user-inputted stock
        volume_week = info.get('averageVolume10days', 'N/A')
        volume_month = info.get('averageVolume', 'N/A')
        volume_year = info.get('averageVolume10days', 'N/A')

        # Create a label for volume data
        volume_label = ttk.Label(self, text=f"Volume (Week): {volume_week} | Volume (Month): {volume_month} | Volume (Year): {volume_year}")
        volume_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Clear the existing earnings data
        self.earnings_label.config(text="")

        # Fetch earnings data using yahoo_fin
        earnings = si.get_earnings(symbol)
        if earnings.empty:
            self.earnings_label.config(text="No earnings data available.")
        else:
            earnings_data = "Earnings Dates: "
            for date in earnings.tail(3)['startdatetime']:
                formatted_date = date.strftime("%Y/%m/%d")
                earnings_info = f"{formatted_date} | "
                earnings_data += earnings_info

            # Remove the last "| " from the earnings_data
            earnings_data = earnings_data.rstrip("| ")

            # Create a label for earnings data
            earnings_label = ttk.Label(self, text=earnings_data)
            earnings_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

def display_company_data(parent):
    option_window = CompanyDataWindow(parent)