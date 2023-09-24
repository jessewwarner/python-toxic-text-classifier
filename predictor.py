import joblib
import model_trainer

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