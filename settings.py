

import tkinter as tk
from tkinter import ttk
import json

class ButtonFunctions:
    def __init__(self, parent_window):
        self.parent_window = parent_window

    def open_settings_window(self):
        settings_window = tk.Toplevel(self.parent_window)
        settings_window.title("Settings")

        label_title = ttk.Label(settings_window, text="Email Controls")
        label_title.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        frame_content = ttk.Frame(settings_window)
        frame_content.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        labels = ["From Address:", "To Address:", "Password location:",
                  "Email frequency (minutes):", "Email start time (hours):",
                  "Email end time (hours):", "Email Alerts:",
                  "Upswing Threshold (%):", "Price Target:"]

        for i, text in enumerate(labels):
            label = ttk.Label(frame_content, text=text)
            label.grid(row=i, column=0, sticky=tk.W)
            entry = ttk.Entry(frame_content)
            entry.grid(row=i, column=1, padx=(10, 0), pady=5, sticky=tk.W+tk.E)

        # Create the Save button
        save_button = ttk.Button(settings_window, text="Save", command=self.save_settings)
        save_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

    def save_settings(self):
        # Get the values from the entry fields
        labels = ["From Address:", "To Address:", "Password location:",
                  "Email frequency (minutes):", "Email start time (hours):",
                  "Email end time (hours):", "Email Alerts:",
                  "Upswing Threshold (%):", "Price Target:"]

        settings = {}
        for label in labels:
            entry = self.get_entry_by_label(label)
            settings[label] = entry.get()

        # Save the settings to the JSON file
        with open("settings.json", "w") as file:
            json.dump(settings, file)

    def get_entry_by_label(self, label_text):
        # Get the entry field corresponding to the given label text
        for child in self.parent_window.winfo_children():
            if isinstance(child, ttk.Entry) and child.get() == label_text:
                return child
        return None

def open_settings_window(parent):
    option_window = ButtonFunctions(parent)