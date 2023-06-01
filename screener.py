import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox

class StockScreenerWindow(tk.Toplevel):
    def __init__(self, parent, stock_data):
        super().__init__(parent)
        self.title("Screener")
        self.stock_data = stock_data

        # Create a frame for the search input
        search_frame = ttk.Frame(self)
        search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        # Create and position the Search label
        search_label = ttk.Label(search_frame, text="Market Cap:")
        search_label.grid(row=0, column=1, padx=5, sticky="we")

        # Create and position the input box for search
        self.search_entry = ttk.Entry(search_frame, width=10)
        self.search_entry.grid(row=0, column=2, sticky="we")

        # Create a frame for the type input
        type_frame = ttk.Frame(self)
        type_frame.grid(row=0, column=1, padx=10, pady=10, sticky="we")

        # Create and position the Type label
        type_label = ttk.Label(type_frame, text="To:")
        type_label.grid(row=0, column=0, padx=5, sticky="we")

        # Create and position the input box for type
        self.type_entry = ttk.Entry(type_frame, width=10)
        self.type_entry.grid(row=0, column=1, sticky="we")

        # Create a frame for the filter button
        filter_frame = ttk.Frame(self)
        filter_frame.grid(row=1, column=0, columnspan=4, pady=10, sticky="we")

        # Create and position the Filter button
        filter_button = ttk.Button(filter_frame, text="Filter", command=self.filter_data)
        filter_button.pack()

        # Create a frame for the table
        table_frame = ttk.Frame(self)
        table_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="we")

        # Create the table columns
        columns = ['Company', 'Market Cap']

        # Create the table
        self.table = ttk.Treeview(table_frame, columns=columns, show='headings')
        self.table.grid(row=0, column=0, sticky="we")

        # Configure column headings
        for col in columns:
            self.table.heading(col, text=col)

        self.table.column("Company", width=1200, anchor="center", uniform="table")
        self.table.column("Market Cap", width=500, anchor="center",  uniform="table")

    def filter_data(self):
        try:
            market_cap_from = float(self.search_entry.get())
            market_cap_to = float(self.type_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for Market Cap.")
            return

        # Filter the stock data based on market cap
        filtered_data = self.stock_data[
            (self.stock_data['Market Cap'] >= market_cap_from) &
            (self.stock_data['Market Cap'] <= market_cap_to)
        ]

        # Clear existing table rows
        for item in self.table.get_children():
            self.table.delete(item)

        # Insert filtered data into the table
        for _, row in filtered_data.iterrows():
            self.table.insert('', 'end', values=[row['Symbol'], row['Market Cap']])

def display_screener(parent):
    # Load stock data from Excel
    stock_data = pd.read_csv('nasdaq_screener_1685462781385.csv')  # Replace 'stock_data.xlsx' with the path to your Excel file

    option_window = StockScreenerWindow(parent, stock_data)