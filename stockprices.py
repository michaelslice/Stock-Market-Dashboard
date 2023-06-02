import tkinter as tk
from tkinter import ttk
import pandas as pd

class StockPricesWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Stock Sectors")

        # Create a frame to hold the buttons and the data table
        content_frame = ttk.Frame(self)
        content_frame.pack(side=tk.TOP,padx=10, pady=10)

        # Create a frame to hold the buttons
        button_frame = ttk.Frame(content_frame)
        button_frame.pack(side=tk.TOP, pady=10)

        # Define the category names and their corresponding sectors
        categories = [
            ("Industrials", "Industrials"),
            ("Consumer discretionary", "Consumer Discretionary"),
            ("Finance", "Finance"),
            ("Health Care", "Health Care"),
            ("Real Estate", "Real Estate"),
            ("Miscellaneous", "Miscellaneous"),
            ("Technology", "Technology"),
            ("Energy", "Energy"),
            ("Utilities", "Utilities"),
            ("Telecommunications", "Telecommunications"),
            ("Consumer Staples", "Consumer Staples"),
            ("Basic Materials", "Basic Materials")
        ]

        # Create buttons for each category and pack them in the button frame
        for category, sector in categories:
            button = ttk.Button(button_frame, text=category)
            button.pack(side=tk.LEFT, padx=5)

            # Bind the button click event to a function that displays the stock names
            button.bind("<Button-1>", lambda event, sector=sector: self.display_stock_names(sector))

        # Create a Treeview widget to display the stock data
        self.treeview = ttk.Treeview(content_frame, columns=("Stock Name", "Stock Sector", "Last Sale", "Net Change", "Market Cap", "Country", "IPO Year", "Volume", "Industry"), show="headings")
        self.treeview.pack(padx=10, pady=(0, 10), fill=tk.BOTH, expand=True)

        # Configure the columns
        self.treeview.heading("Stock Name", text="Stock Name")
        self.treeview.heading("Stock Sector", text="Stock Sector")
        self.treeview.heading("Last Sale", text="Last Sale")
        self.treeview.heading("Net Change", text="Net Change")
        self.treeview.heading("Market Cap", text="Market Cap")
        self.treeview.heading("Country", text="Country")
        self.treeview.heading("IPO Year", text="IPO Year")
        self.treeview.heading("Volume", text="Volume")
        self.treeview.heading("Industry", text="Industry")

        # Set the column widths
        self.treeview.column("Stock Name", width=100)
        self.treeview.column("Stock Sector", width=100)
        self.treeview.column("Last Sale", width=80)
        self.treeview.column("Net Change", width=80)
        self.treeview.column("Market Cap", width=100)
        self.treeview.column("Country", width=80)
        self.treeview.column("IPO Year", width=80)
        self.treeview.column("Volume", width=80)
        self.treeview.column("Industry", width=250)

        try:
            # Read the stock data from the Excel file
            self.stock_data = pd.read_csv('nasdaq_screener_1685462781385.csv')
        except Exception as e:
            print(f"Error reading stock data: {e}")

    def display_stock_names(self, sector):
        # Delete existing rows in the treeview
        self.treeview.delete(*self.treeview.get_children())

        try:
            # Filter the stock data based on the selected sector
            filtered_stocks = self.stock_data[self.stock_data["Sector"] == sector]

            # Insert the filtered stock data into the treeview
            for index, row in filtered_stocks.iterrows():
                self.treeview.insert("", tk.END, values=(
                    row["Symbol"], row["Sector"], row["Last Sale"], row["Net Change"],
                    row["Market Cap"], row["Country"], row["IPO Year"], row["Volume"], row["Industry"]
                ))
        except Exception as e:
            print(f"Error displaying stock names: {e}")

def display_stock_prices(parent):
    option_window = StockPricesWindow(parent)