import tkinter as tk
import predictor
import visualizations
from tkinter import scrolledtext

# Send the comment in the input text box to the model for prediction.
def on_submit_button_click(e=None):
    input_text = input_entry.get()
    status_label.config(text="Determining if the comment is toxic...")
    window.update()
    prediction = predictor.predict(input_text)
    status_label.config(text="Ready.")
    output_text.insert(tk.END, f"{prediction}\n")
    output_text.see(tk.END)

# Create the bar chart showing the toxic comment distribution by number.
def on_bar_chart_num_btn_click():
    status_label.config(text="Creating bar chart...")
    window.update()
    visualizations.create_bar_chart_number()
    status_label.config(text="Ready")

# Create the bar chart showing toxic comments by category
def on_bar_chart_cat_btn_click():
    status_label.config(text="Creating bar chart...")
    window.update()
    visualizations.create_bar_chart_categories()
    status_label.config(text="Ready")

# Create the pie chart showing the percentage of toxic and non-toxic comments
def on_pie_chart_btn_click():
    status_label.config(text="Creating pie chart...")
    window.update()
    visualizations.create_pie_chart()
    status_label.config(text="Ready")

# Create the heatmap that displays the precision, recall, and f1 score metrics.
def on_heatmap_btn_click():
    status_label.config(text="Heatmap is being generated. Please be patient...")
    window.update()
    visualizations.create_heatmap()
    status_label.config(text="Ready")

# Generate and display the model's accuracy using the test dataset.
def on_accuracy_btn_click():
    status_label.config(text="Test dataset is being analyzed. Please be patient...")
    window.update()
    accuracy = predictor.get_accuracy_metric()
    accuracy_label.config(text=f"Accuracy: {accuracy * 100:.2f}%")
    status_label.config(text="Ready")

# Create the main window
window = tk.Tk()
window.title("Toxic Comment Classifier")
window.geometry("800x600")

# Create the text input box and submit button
input_label = tk.Label(window, text="Enter Comment: ")
input_entry = tk.Entry(window)
submit_button = tk.Button(window, text="Submit", command=on_submit_button_click) # Add function
input_label.place(x=20, y=15, width=120)
input_entry.place(x=140, y=10, width=540, height=30)
submit_button.place(x=690, y=10, width=90)

input_entry.bind("<Return>", on_submit_button_click) # Add function

# Create and position output textbox
output_text = scrolledtext.ScrolledText(window)
output_text.place(x=20, y=50, width=760, height=380)

# Status label to show what the program is doing
status_label = tk.Label(window, text="Ready")
status_label.place(x=20, y=435)

# Accuracy label to display the accuracy of the model's predictions.
accuracy_label = tk.Label(window, text="Accuracy: ")
accuracy_label.place(x=20, y=460)

# Create and position the visualization buttons
bar_chart_num_btn = tk.Button(window, text="Show Toxic Comment\nDistribution by Number", command=on_bar_chart_num_btn_click) # Add function
bar_chart_cat_btn = tk.Button(window, text="Show % of Toxic and\nNon-Toxic Comments", command=on_bar_chart_cat_btn_click) # Add function
pie_chart_btn = tk.Button(window, text="Show % of Toxic\nComments by Category", command=on_pie_chart_btn_click) # Add function
heatmap_btn = tk.Button(window, text="Show Heatmap of Precision\nRecall and F1 Score Metrics", command=on_heatmap_btn_click) # Add function
accuracy_btn = tk.Button(window, text="Show Prediction Accuracy\nFor Test Dataset", command=on_accuracy_btn_click) # Add function

bar_chart_num_btn.place(x=20, y=485, width=180)
bar_chart_cat_btn.place(x=210, y=485, width=180)
pie_chart_btn.place(x=400, y=485, width=180)
heatmap_btn.place(x=20, y=535, width=210)
accuracy_btn.place(x=240, y=535, width=180)

window.mainloop()