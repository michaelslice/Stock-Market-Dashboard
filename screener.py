import tkinter as tk
from tkinter import ttk

class StockScreenerWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Option Prices")
        # Add the desired content to the new window


def display_screener(parent):
    option_window = StockScreenerWindow(parent)
