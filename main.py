import tkinter as tk
from tkinter import scrolledtext

import predictor

# Send the comment in the input text box to the model for prediction.
def on_submit_button_click():
    input_text = input_entry.get()
    status_label.config(text="Determining if the comment is toxic...")
    window.update()
    prediction = predictor.predict(input_text)
    status_label.config(text="Ready.")
    output_text.insert(tk.END, f"{prediction}\n")
    output_text.see(tk.END)

def placeHolder(e=''):
    print("hello, world")

# Create the main window
window = tk.Tk()
window.title("Toxic Comment Classifier")
window.geometry("800x600")

# Create the text input box and submit button
input_label = tk.Label(window, text="Enter Comment: ")
input_entry = tk.Entry(window)
submit_button = tk.Button(window, text="Submit", command=placeHolder) # Add function
input_label.place(x=20, y=15, width=120)
input_entry.place(x=140, y=10, width=540, height=30)
submit_button.place(x=690, y=10, width=90)

input_entry.bind("<Return>", placeHolder) # Add function

# Create and position output textbox
output_text = scrolledtext.ScrolledText(window)
output_text.place(x=20, y=50, width=760, height=380)

# Status label to show what the program is doing
status_label = tk.Label(window, text="Ready")
status_label.place(x=20, y=435)

# Accuracy label to display the accuracy of the model's predictions.
accuracy_label = tk.Label(window, text="Accuracy: ")
accuracy_label.place(x=20, y=460)

# Create the buttons
bar_chart_btn = tk.Button(window, text="Show Toxic Comment\nDistribution by Number", command=placeHolder) # Add function
pie_chart_btn_one = tk.Button(window, text="Show % of Toxic and\nNon-Toxic Comments", command=placeHolder) # Add function
pie_chart_btn_two = tk.Button(window, text="Show % of Toxic\nComments by Category", command=placeHolder) # Add function
heatmap_btn = tk.Button(window, text="Show Heatmap of Precision\nRecall and F1 Score Metrics", command=placeHolder) # Add function
accuracy_btn = tk.Button(window, text="Show Prediction Accuracy\nFor Test Dataset", command=placeHolder) # Add function

bar_chart_btn.place(x=20, y=485, width=180)
pie_chart_btn_one.place(x=210, y=485, width=180)
pie_chart_btn_two.place(x=400, y=485, width=180)
heatmap_btn.place(x=20, y=535, width=210)
accuracy_btn.place(x=240, y=535, width=180)

window.mainloop()