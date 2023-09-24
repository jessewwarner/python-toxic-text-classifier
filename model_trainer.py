import joblib
import data_handler
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multioutput import MultiOutputClassifier


# Create the machine learning model and vectorizer and store them locally.
def create_model():
    train_x, test_x, train_y, test_y = data_handler.get_train_test_sets()

    vector_algo = TfidfVectorizer()
    trainXVector = vector_algo.fit_transform(train_x)

    joblib.dump(vector_algo, 'Vectorizer.pkl')

    toxic_predictor = MultiOutputClassifier(RandomForestClassifier(n_estimators=125))
    toxic_predictor.fit(trainXVector, train_y)

    joblib.dump(toxic_predictor, 'ToxicCommentClassifier.pkl')

    return toxic_predictor

# Creates and returns a vectorizer for the model to use.
# NOTE: this should not need to be called as one is created and stored locally 
# as Vectorizer.pkl, but it is here incase it was deleted or moved.
def create_vectorizer():
    train_x, test_x, train_y, test_y = data_handler.get_train_test_sets()

    # Convert the comments to a numerical form so the algorithm can operate on 
    # them. The Term Frequency-Inverse Document Frequency (TF-IDF) technique 
    # is used.
    vectorAlgo = TfidfVectorizer()
    vectorAlgo.fit_transform(train_x)
    vectorAlgo.transform(test_x)
    joblib.dump(vectorAlgo, 'Vectorizer.pkl')

    return vectorAlgo