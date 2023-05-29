
#BUTTONS STAY THE SAME AND CODE IS OK
import tkinter as tk
from tkinter import ttk
import yfinance as yf

class OptionWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Option Prices")
        self.title("Option Prices")
        self.geometry("800x400")  # Set a fixed size for the window

        self.resizable(False, False)

        # Create a frame for the search input
        search_frame = ttk.Frame(self)
        search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        # Create and position the Search label
        search_label = ttk.Label(search_frame, text="Search:")
        search_label.grid(row=0, column=0, padx=5, sticky="we")

        # Create and position the input box for search
        self.search_entry = ttk.Entry(search_frame, width=10)
        self.search_entry.grid(row=0, column=1, sticky="we")

        # Create a frame for the type input
        type_frame = ttk.Frame(self)
        type_frame.grid(row=0, column=1, padx=10, pady=10, sticky="we")

        # Create and position the Type label
        type_label = ttk.Label(type_frame, text="Type:")
        type_label.grid(row=0, column=0, padx=5, sticky="we")

        # Create and position the input box for type
        self.type_entry = ttk.Entry(type_frame, width=10)
        self.type_entry.grid(row=0, column=1, sticky="we")

        # Create a frame for the expiration date input
        exp_date_frame = ttk.Frame(self)
        exp_date_frame.grid(row=0, column=2, padx=10, pady=10, sticky="we")

        # Create and position the Expiration Date label
        exp_date_label = ttk.Label(exp_date_frame, text="Exp. Date:")
        exp_date_label.grid(row=0, column=0, padx=5, sticky="we")

        # Create and position the input box for expiration date
        self.exp_date_entry = ttk.Entry(exp_date_frame, width=10)
        self.exp_date_entry.grid(row=0, column=1, sticky="we")

        # Create a frame for the strike price input
        strike_price_frame = ttk.Frame(self)
        strike_price_frame.grid(row=0, column=3, padx=10, pady=10, sticky="we")

        # Create and position the Strike Price label
        strike_price_label = ttk.Label(strike_price_frame, text="Strike Price:")
        strike_price_label.grid(row=0, column=0, padx=5, sticky="we")
        


        # Create and position the input box for strike price
        self.strike_price_entry = ttk.Entry(strike_price_frame, width=10)
        self.strike_price_entry.grid(row=0, column=1, sticky="we")

        # Create a frame for the filter button
        filter_frame = ttk.Frame(self)
        filter_frame.grid(row=1, column=0, columnspan=4, pady=10, sticky="we")
  

        # Create and position the Filter button
        filter_button = ttk.Button(filter_frame, text="Filter", command=self.perform_filter)
        filter_button.pack()

        # Create a frame for displaying the option pricing table
        self.table_frame = ttk.Frame(self)
        self.table_frame.grid(row=2, column=0, columnspan=4, padx=(20,10), pady=10, sticky="ew")

        # Create the treeview widget for displaying the option pricing table
        columns = ["Expiration", "Type", "Strike", "Last Price", "Bid", "Ask", "Change", "% Change", "Volume", "Open Interest", "Implied Vol"]
       
        self.tree = ttk.Treeview(self.table_frame, show="headings", columns=columns )
        self.tree.grid(row=0, column=0, sticky="we")

        # Configure row height
        self.tree.configure(height=10)  # Adjust the row height as needed

        # Create a scrollbar for the treeview
        tree_scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.tree.yview)
        tree_scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=tree_scrollbar.set)

        # Configure column headers and widths
        header_widths = [65, 60, 60, 70, 60, 60, 60, 70, 50, 100, 100, 0]   # Set a default width of 80 for each column
        for col, width in zip(columns, header_widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center", stretch=False)  # Set stretch=False to disable column resizing

        # Configure grid weights to make the table frame expand with the window
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="equal")

    

        # Configure grid weights to make the table frame expand with the window
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

     
    def perform_filter(self):
        # Get the values from the input fields
        search_term = self.search_entry.get()
        option_type = self.type_entry.get()
        exp_date = self.exp_date_entry.get()
        strike_price = self.strike_price_entry.get()

        # Fetch option data using yfinance
        option_chain = self.get_option_quotes(search_term)

        if option_chain is not None:
            # Clear any previous content from the table frame
            self.tree.delete(*self.tree.get_children())
            option_chain.drop("contractSymbol", axis=1, inplace=True)
            option_chain.drop("lastTradeDate", axis=1, inplace=True)
            option_chain.drop("currency", axis=1, inplace=True)
            option_chain.drop("inTheMoney", axis=1, inplace=True)
            option_chain.drop("contractSize", axis=1, inplace=True)

            # Filter the option data based on the input values
            if option_type:
                option_chain = option_chain[option_chain["Type"] == option_type]
            if exp_date:
                option_chain = option_chain[option_chain["Expiration"] == exp_date]
            if strike_price:
                option_chain = option_chain[option_chain["Strike"] == float(strike_price)]

            # Set table columns
            columns = ["Expiration", "Type", "Strike", "Last Price", "Bid", "Ask", "Change", "% Change", "Volume", "Open Interest", "Implied Vol"]
            self.tree["columns"] = columns

            # Calculate the maximum width of the column headers
            max_header_width = max(len(col) for col in columns)

            # Configure column headers and widths
            for col in columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=max_header_width * 5, stretch=0)  # Adjust the column width multiplier as needed

            # Insert option chain data
            for i, row in option_chain.iterrows():
                self.tree.insert("", "end", values=row.tolist())

    @staticmethod
    def get_option_quotes(stock_symbol):
        try:
            # Fetch option data using yfinance
            ticker = yf.Ticker(stock_symbol)
            option_chain = ticker.option_chain()

            return option_chain.calls if option_chain is not None else None
        except Exception as e:
            print("Error fetching option data:", str(e))
            return None

def display_option_prices(parent):
    option_window = OptionWindow(parent)
    