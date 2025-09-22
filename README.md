# 🔍 Phishing URL Detection

A machine learning project that detects **phishing URLs** based only on URL-based lexical features (94 features).
The project includes:

* A **trained ML model** (`tuned_xgboost_model.pkl`)
* A **feature extractor** (`feature_extractor.py`)
* A **Streamlit frontend** (`app.py`) for easy web-based testing
* A **Flask backend** option for API deployment

---

## 🚀 Features

* Extracts **94 lexical features** from any given URL
* Classifies URL as **Phishing** or **Legitimate**
* Shows model’s **confidence score**
* Provides both **API** (Flask) and **UI** (Streamlit) usage

---

## 📂 Project Structure

```
├── app.py                # Streamlit app for user interface
├── feature_extractor.py  # Extracts 94 features from a URL
├── predict.py            # Helper for standalone predictions
├── model.pkl             # Trained ML model
├── requirements.txt      # Python dependencies
├── test_request.py       # Example request to Flask API
└── README.md             # Project documentation
```

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/phishing-url-detection.git
cd phishing-url-detection
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Run with Streamlit (Web UI)

```bash
streamlit run app.py
```

* Enter a URL in the textbox
* Click **Check URL**
* Get **Prediction + Confidence Score**

---

### 2. Run Flask API (Backend)

```bash
python app.py
```

Then send a POST request with a URL:

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"url\":\"http://example.com\"}"
```

Expected Response:

```json
{
  "prediction": "Phishing",
  "probability": 0.988,
  "url": "http://example.com"
}
```

---

### 3. Test with Python request script

```bash
python test_request.py
```

---

## 📊 Model & Features

* Extracts **94 lexical features** such as:

  * `qty_dot_url`, `qty_hyphen_url`, `length_url`, `domain_length`, etc.
* Model trained on phishing vs legitimate URLs dataset.
* Saved as `model.pkl` (scikit-learn compatible).

---

## ⚡ Future Work

* Improve accuracy with **deep learning models**
* Add **real-time browser extension**
* Integrate with **threat intelligence APIs** for hybrid detection

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📜 License

This project is licensed under the MIT License.

---
