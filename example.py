import pickle
from sklearn.ensemble import RandomForestClassifier
def predict(text: str, model_type: str, dataset_name: str):
    with open('vectorizer.pkl', 'rb') as file:
        vectorizer = pickle.load(file)
    model = load_model(model_type, dataset_name)
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    print(prediction)


def load_model(model_type, dataset_name):
    """
    Load a pre-trained model from disk.

    This function opens a pickle file named with the model type and dataset name,
    loads the model from the file, and then returns the model.

    Parameters:
    model_type (str): The type of the model to load (e.g., 'nb', 'rf', 'dt', 'knn', 'lg').
    dataset_name (str): The name of the dataset the model was trained on (e.g., 'twitter', 'movie').

    Returns:
    model: The loaded model.
    """
    with open(f'models/{model_type}_{dataset_name}.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# demo
# predict('I love this movie!', 'rf', 'twitter')