import pickle
import numpy as np
from feature_extractor import feature_extractor

# Load model
with open("tuned_xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict(url: str):
    features = feature_extractor(url)
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]  # phishing class prob
    return prediction, probability

if __name__ == "__main__":
    test_url = "http://example.com/test"
    pred, prob = predict(test_url)
    print("Prediction:", "Phishing" if pred == 1 else "Legit")
    print("Phishing Probability:", prob)
