import streamlit as st
import joblib
import pandas as pd
from feature_extractor import feature_extractor

# Load trained model
model = joblib.load("tuned_xgboost_model.pkl")

st.title("🔒 Phishing URL Detector")

# Input box
url = st.text_input("Enter a URL to check:")

if st.button("Predict"):
    if url:
        # Extract features
        features = extract_features(url)   # must return a dict with all 94 features
        df = pd.DataFrame([features])      # convert dict → DataFrame
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]

        if prediction == 1:
            st.error(f"🚨 Phishing (Probability: {probability:.2f})")
        else:
            st.success(f"✅ Legitimate (Probability: {1-probability:.2f})")
    else:
        st.warning("Please enter a URL")
