import streamlit as st
import joblib
import pandas as pd
from feature_extractor import feature_extractor

# Load model
@st.cache_resource
def load_model():
    return joblib.load("tuned_xgboost_model.pkl")

model = load_model()

# Define label mapping (adjust if your dataset used opposite encoding)
label_map = {
    0: "Phishing",
    1: "Legitimate"
}

st.title("🔍 Phishing URL Detection")

url = st.text_input("Enter a URL to check:")

if st.button("Check URL"):
    if url.strip():
        try:
            # Extract 94 features → DataFrame
            df = feature_extractor(url)

            # Predict class
            prediction = model.predict(df)[0]

            # Get probability for predicted class
            proba = model.predict_proba(df)[0]
            class_index = list(model.classes_).index(prediction)
            probability = proba[class_index]

            # Map numeric label → readable
            prediction_label = label_map.get(prediction, str(prediction))

            # Show results
            st.success(f"Prediction: **{prediction_label}**")
            st.info(f"Confidence: {probability:.2%}")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid URL.")
