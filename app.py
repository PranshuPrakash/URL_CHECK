from flask import Flask, request, jsonify
from predict import predict

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict_url():
    data = request.json
    if not data or "url" not in data:
        return jsonify({"error": "No URL provided"}), 400
    
    url = data["url"]
    try:
        pred, prob = predict(url)
        return jsonify({
            "url": url,
            "prediction": "Phishing" if pred == 1 else "Legit",
            "probability": float(prob)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
