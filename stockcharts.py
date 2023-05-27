
import tkinter as tk
from tkinter import ttk
import yfinance as yf
import plotly.graph_objects as go

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
    
    def perform_search(self):
        # Get the stock ticker from the input box
        stock_ticker = self.entry_var.get()
        
        # Perform the search operation and display the stock graph
        data = fetch_stock_data(stock_ticker)
        
        if data is not None:
            self.display_stock_graph(data)
        else:
            print(f"Unable to retrieve stock data for {stock_ticker}.")
    
    def display_stock_graph(self, data):
        # Clear any previous graph from the graph frame
        for child in self.graph_frame.winfo_children():
            child.destroy()
    
    # Filter the stock data based on the selected time frame
        filtered_data = self.filter_data_by_time_frame(data)
        
        # Create the stock graph using Plotly
        fig = go.Figure(data=[go.Candlestick(x=filtered_data['Date'],
                                             open=filtered_data['Open'],
                                             high=filtered_data['High'],
                                             low=filtered_data['Low'],
                                             close=filtered_data['Close'])])
        
        # Create the Plotly graph widget
        graph_widget = go.FigureWidget(fig)
        graph_widget.update_layout(height=400, margin=dict(t=10, b=10, r=10, l=10))
        graph_widget.update_yaxes(fixedrange=True)  # Disable zooming on y-axis
        
        # Embed the Plotly graph widget into the graph frame
        graph_widget_frame = graph_widget.to_image(format="png")
        graph_widget_label = ttk.Label(self.graph_frame, image=graph_widget_frame)
        graph_widget_label.image = graph_widget_frame
        graph_widget_label.pack(expand=True, fill="both")
        
    def filter_data_by_time_frame(self, data):
        if self.begin_date and self.end_date:
            # Filter the data based on the selected time frame
            mask = (data['Date'] >= self.begin_date) & (data['Date'] <= self.end_date)
            filtered_data = data.loc[mask]
            return filtered_data
        else:
            return data
    
    def set_begin_time_frame(self):
        # Implement logic to set the beginning time frame for the stock graph
        begin_date = self.begin_entry_var.get()
        # Perform any required processing or validation
        self.begin_date = begin_date
    
    def set_end_time_frame(self):
        # Implement logic to set the ending time frame for the stock graph
        end_date = self.end_entry_var.get()
        # Perform any required processing or validation
        self.end_date = end_date
    
def fetch_stock_data(stock_ticker):
    try:
        # Fetch stock data using yfinance
        stock_data = yf.download(stock_ticker)
        
        # Process the stock data (if required)
        if not stock_data.empty:
            # Select only the required columns (Date, Open, High, Low, Close)
            stock_data = stock_data[['Date', 'Open', 'High', 'Low', 'Close']]
            
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
