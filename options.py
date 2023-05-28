
import tkinter as tk
from tkinter import ttk
import yfinance as yf
from datetime import datetime, timedelta

class OptionWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Option Prices")

        # Create a frame for the search input
        search_frame = ttk.Frame(self)
        search_frame.grid(row=0, column=0, padx=10, pady=10)

        # Create and position the Search label
        search_label = ttk.Label(search_frame, text="Search:")
        search_label.grid(row=0, column=0, padx=5)

        # Create and position the input box for search
        self.search_entry = ttk.Entry(search_frame, width=10)
        self.search_entry.grid(row=0, column=1)

        # Create a frame for the type input
        type_frame = ttk.Frame(self)
        type_frame.grid(row=0, column=1, padx=10, pady=10)

        # Create and position the Type label
        type_label = ttk.Label(type_frame, text="Type:")
        type_label.grid(row=0, column=0, padx=5)

        # Create and position the input box for type
        self.type_entry = ttk.Entry(type_frame, width=10)
        self.type_entry.grid(row=0, column=1)

        # Create a frame for the expiration date input
        exp_date_frame = ttk.Frame(self)
        exp_date_frame.grid(row=0, column=2, padx=10, pady=10)

        # Create and position the Expiration Date label
        exp_date_label = ttk.Label(exp_date_frame, text="Exp. Date:")
        exp_date_label.grid(row=0, column=0, padx=5)

        # Create and position the input box for expiration date
        self.exp_date_entry = ttk.Entry(exp_date_frame, width=10)
        self.exp_date_entry.grid(row=0, column=1)

        # Create a frame for the strike price input
        strike_price_frame = ttk.Frame(self)
        strike_price_frame.grid(row=0, column=3, padx=10, pady=10)

        # Create and position the Strike Price label
        strike_price_label = ttk.Label(strike_price_frame, text="Strike Price:")
        strike_price_label.grid(row=0, column=0, padx=5)

        # Create and position the input box for strike price
        self.strike_price_entry = ttk.Entry(strike_price_frame, width=10)
        self.strike_price_entry.grid(row=0, column=1)

        # Create a frame for the filter button
        filter_frame = ttk.Frame(self)
        filter_frame.grid(row=1, column=0, columnspan=4, pady=10)

        # Create and position the Filter button
        filter_button = ttk.Button(filter_frame, text="Filter", command=self.perform_filter)
        filter_button.pack()

        # Create a frame for displaying the option pricing table
        self.table_frame = ttk.Frame(self)
        self.table_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    def perform_filter(self):
        # Get the values from the input fields
        search_term = self.search_entry.get()
        option_type = self.type_entry.get()
        exp_date = self.exp_date_entry.get()
        strike_price = self.strike_price_entry.get()

        # Fetch option data using yfinance
                # Fetch option data using yfinance
        option_data = yf.Ticker(search_term).option_chain(date=exp_date)

        # Validate the fetched option data
        if option_data:
            # Filter the option data based on the user's inputs
            filtered_data = option_data[(option_data['Type'] == option_type) &
                                        (option_data['Strike'] == float(strike_price))]

            # Clear any previous content from the table frame
            for child in self.table_frame.winfo_children():
                child.destroy()

            # Create a text widget to display the option pricing table
            table_text = tk.Text(self.table_frame, width=60)
            table_text.pack()

            # Display the option pricing table
            table_text.insert(tk.END, filtered_data.to_string(index=False))
        else:
            print("Unable to fetch option data.")


def display_option_prices(parent):
    option_window = OptionWindow(parent)
