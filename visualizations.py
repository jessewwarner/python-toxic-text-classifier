import matplotlib.pyplot as plot
import numpy as np
import data_handler

# Shows a barchart of the data distribution by number.
def create_bar_chart():
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