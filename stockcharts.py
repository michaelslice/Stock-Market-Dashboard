import tkinter as tk
from tkinter import ttk
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mplcursors


class StockChartWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Stock Charts")

        # Set window size and position
        window_width = 800
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create a frame for the input box and time frame labels
        input_frame = ttk.Frame(self)
        input_frame.pack(pady=20)

        # Create and position the input box
        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(input_frame, textvariable=self.entry_var, width=10)
        self.entry.grid(row=0, column=1)

        # Create and position the Search label
        self.search_label = ttk.Label(input_frame, text="Search:")
        self.search_label.grid(row=0, column=0, padx=5)

        # Create and position the Begin label
        self.begin_label = ttk.Label(input_frame, text="Begin:")
        self.begin_label.grid(row=0, column=2, padx=5)

        # Create and position the End label
        self.end_label = ttk.Label(input_frame, text="End:")
        self.end_label.grid(row=0, column=4, padx=5)

        # Create and position the Begin input box
        self.begin_entry_var = tk.StringVar()
        self.begin_entry = ttk.Entry(input_frame, textvariable=self.begin_entry_var, width=10)
        self.begin_entry.grid(row=0, column=3)

        # Create and position the End input box
        self.end_entry_var = tk.StringVar()
        self.end_entry = ttk.Entry(input_frame, textvariable=self.end_entry_var, width=10)
        self.end_entry.grid(row=0, column=5)

        # Create a frame for displaying the stock graph
        self.graph_frame = ttk.Frame(self)
        self.graph_frame.pack(expand=True, fill="both")

        # Create and position the Filter button
        self.filter_button = ttk.Button(input_frame, text="Filter", command=self.perform_filter)
        self.filter_button.grid(row=1, column=2, pady=10)

        # Initialize the time frame variables
        self.begin_date = None
        self.end_date = None

        # Validate input in the entry box
        self.entry_var.trace("w", self.validate_input)

    def validate_input(self, *args):
        # Get the current value from the entry box
        value = self.entry_var.get()

        # Limit the input to a maximum of 4 characters
        if len(value) > 4:
            self.entry_var.set(value[:4])

        # Ensure the input is uppercase
        self.entry_var.set(value.upper())

    def perform_filter(self):
        # Get the stock ticker from the input box
        stock_ticker = self.entry_var.get()
                # Get the begin date from the input box
        begin_date = self.begin_entry_var.get()
        # Get the end date from the input box
        end_date = self.end_entry_var.get()

        # Perform the search operation and display the stock graph
        data = fetch_stock_data(stock_ticker)

        if data is not None:
            filtered_data = self.filter_data_by_time_frame(data, begin_date, end_date)
            self.display_stock_graph(filtered_data)
        else:
            print(f"Unable to retrieve stock data for {stock_ticker}.")

    def display_stock_graph(self, data):
        # Clear any previous graph from the graph frame
        for child in self.graph_frame.winfo_children():
            child.destroy()

        # Create the stock graph using Matplotlib
        plt.figure(figsize=(10, 6))
        plt.plot(data['Date'], data['Close'], label='Close')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Stock Chart')
        plt.legend()

        # Enable cursor highlighting with data values
        mplcursors.cursor(hover=True)

        # Embed the Matplotlib graph into the graph frame
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")

    def filter_data_by_time_frame(self, data, begin_date, end_date):
        if begin_date and end_date:
            # Filter the data based on the selected time frame
            mask = (data['Date'] >= begin_date) & (data['Date'] <= end_date)
            filtered_data = data.loc[mask]
            return filtered_data
        else:
            return data


def fetch_stock_data(stock_ticker):
    try:
        # Fetch stock data using yfinance
        stock_data = yf.download(stock_ticker)

        # Process the stock data (if required)
        if not stock_data.empty:
            # Reset the index
            stock_data.reset_index(inplace=True)
            return stock_data
        else:
            print(f"No data available for stock ticker: {stock_ticker}")
            return None
    except Exception as e:
        print(f"Error fetching stock data for {stock_ticker}: {str(e)}")
        return None

def display_stock_charts(parent):
    option_window = StockChartWindow(parent)