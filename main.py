import tkinter as tk
from tkinter import scrolledtext

# Create the main window
window = tk.Tk()
window.title("Toxic Comment Classifier")
window.geometry("800x600")

# Create the text input box and submit button
inputLabel = tk.Label(window, text="Enter Comment: ")
inputEntry = tk.Entry(window)

# Configure the input label, input entry, and submit button to span the width of the window
inputLabel.pack(side="left", anchor="n", padx=10, pady=10)
inputEntry.pack(side="top", fill="x", padx=10, pady=10)

window.mainloop()