import tkinter as tk
from tkinter import ttk

class ButtonFunctions:
    def __init__(self, parent_window):
        self.parent_window = parent_window

    def open_settings_window(self):
        settings_window = tk.Toplevel(self.parent_window)
        settings_window.title("Settings")

        # Add content to the settings window as needed

        # Example content: Label and Button
        label = ttk.Label(settings_window, text="This is the settings window.")
        label.pack(padx=10, pady=10)

        button = ttk.Button(settings_window, text="Close", command=settings_window.destroy)
        button.pack(padx=10, pady=10)



def open_settings_window(parent):
    option_window = ButtonFunctions(parent)