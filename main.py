import tkinter as tk
from tkinter import scrolledtext

def placeHolder():
    pass

# Create the main window
window = tk.Tk()
window.title("Toxic Comment Classifier")
window.geometry("800x600")

# Create the text input box and submit button
inputLabel = tk.Label(window, text="Enter Comment: ")
inputEntry = tk.Entry(window)
inputEntry.bind("<Return>", placeHolder) # Add function
submitButton = tk.Button(window, text="Submit", command=placeHolder) # Add function

outputText = scrolledtext.ScrolledText(window, width=90, height=20)

# Configure the input label, input entry, and submit button to span the width of the window
inputLabel.pack(side="top", anchor="w", padx=10, pady=10)
inputEntry.pack(side="top", fill="x", padx=10, pady=10)
submitButton.pack(side="top", anchor="e", padx=10, pady=(0, 10))

# Output window
outputText.pack(side="top", fill="both", padx=10, pady=10)

# Create the buttons
barChartButton = tk.Button(window, text="Show Bar Chart", command=placeHolder) # Add function
pieChartButton = tk.Button(window, text="Show Pie Chart", command=placeHolder) # Add function
heatmapButton = tk.Button(window, text="Show Heatmap", command=placeHolder) # Add function

# Position the buttons
buttonFrame = tk.Frame(window)
buttonFrame.pack(side="bottom", pady=10)
barChartButton.pack(side="left", padx=(10, 5))
pieChartButton.pack(side="left", padx=5)
heatmapButton.pack(side="left", padx=(5, 10))



window.mainloop()