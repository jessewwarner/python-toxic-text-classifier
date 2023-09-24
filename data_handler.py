import pandas
import zipfile
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.model_selection import train_test_split

# Returns data from a csv file within a zipfile as a pandas.read_csv object.
def get_csv_from_zip(zip_file, csv_file):
    # Extract the data from the CSV files within the zip file.
    with zipfile.ZipFile(zip_file, 'r') as train_zip:
        with train_zip.open(csv_file) as train_file:
            csv_data = pandas.read_csv(train_file)

    return csv_data

def clean_data(data):
    data = data.str.lower()
    data = data.apply(lambda i: re.sub(r"[^a-zA-Z]", " ", i))
    data = data.apply(word_tokenize)

    # Remove words that do not provide meaningful data.
    stop_words = stopwords.words("english")
    data = data.apply(lambda i: [word for word in i if word not in stop_words])

    # Convert words to their root form.
    root_words = WordNetLemmatizer()
    data = data.apply(lambda i: [root_words.lemmatize(word) for word in i])

    # Join the words back into sentences
    data = data.apply(lambda i: " ".join(i))

    # Return cleaned data.
    return data

def get_train_test_sets():
    toxic_labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
    # Zip file must be in data folder
    data = get_csv_from_zip('data/toxic_subset_10901.zip', 'toxic_subset_10901.csv')
    data_y = data[toxic_labels]
    # Get cleaned data
    cleaned_comments = clean_data(data['comment_text'])

    return train_test_split(cleaned_comments, data_y, test_size=0.25, random_state=50)