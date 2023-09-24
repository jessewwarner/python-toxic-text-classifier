import joblib
import pandas
import data_handler
import model_trainer

from io import StringIO

model = None
vectorizer = None

# Returns the model. If the model is None, it attempts to load an existing 
# model. If the model isn't found, a new model is created and saved locally.
def get_model():
    global model
    if model is None:
        try:
            model = joblib.load('ToxicCommentClassifier.pkl')
        except FileNotFoundError:
            model = model_trainer.create_model()
    return model

# Returns the vectorizer. If the vectorizer is None, it attempts to load an
# existing vectorizer. If the vectorizer isn't found, a new vectorizer is 
# created and saved locally.
def get_vectorizer():
    global vectorizer
    if vectorizer is None:
        try:
            vectorizer = joblib.load('Vectorizer.pkl')
        except FileNotFoundError:
            vectorizer = model_trainer.create_vectorizer()
    return vectorizer

# Uses the model and vectorizer to make a prediction about whether a comment
# would be considered toxic..
def predict(comment):
    # Formats the comment to be converted to a pandas data object, so it works
    # correctly with the dataHandler.cleandata() function.
    test_string = f'''comment_text
    {comment}'''
    ioStr = StringIO(test_string)
    test_data = pandas.read_csv(ioStr)
    cleaned_comment = data_handler.clean_data(test_data['comment_text'])

    # Vectorize the cleaned comment.
    vectorized_data = get_vectorizer().transform(cleaned_comment)

    # Send the vectorized comment to the model to make a prediction.
    prediction = get_model().predict(vectorized_data)

    # Format the results of the prediction and return them.
    result = prediction[0]
    labels = ['toxic', 'severely toxic', 'obscene', 'threatening', 'insulting',
              'identity hate']
    count = sum(prediction[0])
    response = f'The comment, "{comment}" is '
    toxic_labels = []

    for label, number in zip(labels, result):
        if number == 1:
            toxic_labels.append(label)

    toxic_string = ""
    if len(toxic_labels) == 1:
        toxic_string = toxic_labels[0]
    elif len(toxic_labels) == 2:
        toxic_string = " and ".join(toxic_labels)
    elif len(toxic_labels) > 2:
        try:
            toxic_string = ", ".join(toxic_labels[:-1])
            + ", and "
            + toxic_labels[-1]
        except IndexError:
            pass

    if count == 0:
        response += "non-toxic."
    else:
        response += toxic_string

    return response