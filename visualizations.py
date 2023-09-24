import matplotlib.pyplot as plot
import numpy as np
import data_handler
import predictor

# Shows a barchart of the toxic comment distribution by number.
def create_bar_chart_number():
    # Count the number of comments for each toxicity category.
    data = data_handler.get_csv_from_zip('data/toxic_subset_10901.zip', 'toxic_subset_10901.csv')
    data_columns = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
    counts = [sum(data[column] == 1) for column in data_columns]
    categories = ['Toxic', 'Severe Toxic', 'Obscene', 'Threat', 'Insult', 'Identity Hate', 'Non-toxic']

    # Total the number of comments that do not have toxic traits
    toxic_comment_count = 0
    for index, row in data.iterrows():
        if any(row[column] == 1 for column in data_columns):
            toxic_comment_count += 1

    counts.append(len(data) - toxic_comment_count)

    # Set up the bar chart.
    plot.figure()
    x = np.arange(len(categories))
    plot.bar(x, counts)
    plot.xlabel('Toxicity Category')
    plot.ylabel('Count')
    plot.title('Toxic Comment Distribution by Number\nNote: Some comments fall into multiple categories.')

    # Adjust the subplots so all data is visible
    plot.subplots_adjust(bottom=0.3)

    # Rotate the x-axis labels for improved readability.
    plot.xticks(x, categories, rotation=45)

    plot.show()

def create_bar_chart_categories():
    # Define the toxic categories and their corresponding percentages
    data = data_handler.get_csv_from_zip('toxic_subset_10901.zip', 'toxic_subset_10901.csv')
    data_columns = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
    categories = ['Toxic', 'Severe Toxic', 'Obscene', 'Threat', 'Insult', 'Identity Hate']
    counts = [sum(data[column] == 1) for column in data_columns]

    # Total the number of comments that do not have toxic traits
    toxic_comment_count = 0
    for index, row in data.iterrows():
        if any(row[column] == 1 for column in data_columns):
            toxic_comment_count += 1

    # Calculate the percentages for toxic comment distribution
    percentages = [(i / toxic_comment_count) * 100 for i in counts]

    # Set up the bar chart.
    plot.figure()
    x = np.arange(len(categories))
    plot.bar(x, percentages)
    plot.xlabel('Toxicity Category')
    plot.ylabel('Percentage of Toxic Comments')
    plot.title('Toxic Comment Category Distribution by Percentage\nNote: Some comments fall into multiple categories.')

    # Adjust the subplots so all data is visible
    plot.subplots_adjust(bottom=0.3)

    # Rotate the x-axis labels for improved readability.
    plot.xticks(x, categories, rotation=45)

    plot.tight_layout()
    plot.show()

# Shows a pie chart of the toxic comment distribution by percentages.
def create_pie_chart():
    # Define the toxic categories and their corresponding percentages
    data = data_handler.get_csv_from_zip('toxic_subset_10901.zip', 'toxic_subset_10901.csv')
    data_columns = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
    categories = ['Toxic', 'Non-toxic']
    counts = [sum(data[column] == 1) for column in data_columns]

    total_data = len(data)

    # Total the number of comments that do not have toxic traits
    toxic_comment_count = 0
    for index, row in data.iterrows():
        if any(row[column] == 1 for column in data_columns):
            toxic_comment_count += 1

    # Percentages of toxic and non-toxic comments
    percent_toxic = toxic_comment_count / total_data
    percent_non_toxic = 1 - percent_toxic

    # Calculate the percentages for toxic comment distribution
    percentages = [percent_toxic, percent_non_toxic]

    # Create the pie chart
    plot.figure()
    plot.pie(percentages, labels=None)
    plot.title('Toxic and Non-Toxic Comment\nDistribution by Percentage')

    # Format the text for the legend
    labels = [f'{category} ({(percentage * 100):.2f}%)' for category, percentage in zip(categories, percentages)]

    # Adjust the legend, so it is not on top of the pie chart.
    plot.legend(labels, loc='lower left', bbox_to_anchor=(0.86, 0.0))
    plot.tight_layout()

    plot.show()

# Create a heatmap of the classification report data produced by sklearn metrics
def createHeatMap():
    report_data = predictor.get_classification_report()
    # Get precision, recall, and F1-score data for each category
    categories = list(report_data.keys())
    metrics = ['precision', 'recall', 'f1-score']
    data = np.zeros((len(categories), len(metrics)))

    for i, category in enumerate(categories):
        for j, metric in enumerate(metrics):
            data[i, j] = report_data[category][metric]

    # Create a heatmap using Matplotlib
    figure, axis = plot.subplots()
    heatmap = axis.imshow(data, cmap='coolwarm', vmin=0, vmax=1)

    # Set the ticks on the value bar
    axis.set_xticks(np.arange(len(metrics)))
    axis.set_yticks(np.arange(len(categories)))

    # Set the correct labels
    label_y = ['Toxic', 'Severe Toxic', 'Obscene', 'Threat', 'Insult', 'Identity Hate', 'Micro Average', 'Macro Average',
              'Weighted Average', 'Samples Average']
    label_x = ['Precision', 'Recall', 'F1-Score']
    axis.set_xticklabels(label_x)
    axis.set_yticklabels(label_y)

    # Rotate the tick labels and set alignment for better readability
    plot.setp(axis.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Add colorbar
    colorbar = plot.colorbar(heatmap)
    colorbar.set_label('Value')

    # Add values to the heatmap
    for i in range(len(categories)):
        for j in range(len(metrics)):
            text = axis.text(j, i, f'{data[i, j]:.2f}', ha='center', va='center', color='black')

    plot.title('Classification Report Heatmap')
    plot.xlabel('Metrics')
    plot.ylabel('Categories')
    plot.tight_layout()
    plot.subplots_adjust(bottom=0.18, top=0.94, right=0.75)

    plot.show()