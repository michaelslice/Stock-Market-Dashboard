import tkinter as tk
from tkinter import ttk

class StockChartWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Option Prices")
        # Add the desired content to the new window


def display_stock_charts(parent):
    option_window = StockChartWindow(parent)



   