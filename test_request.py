import requests

url = "http://127.0.0.1:5000/predict"   # Flask server endpoint
data = {"url": "http://example.com/test"}  # test input

try:
    response = requests.post(url, json=data)

    print("Status Code:", response.status_code)
    print("Raw Response Text:", response.text)

    # If JSON is valid, print parsed result
    try:
        print("JSON:", response.json())
    except Exception:
        print("Response is not valid JSON")

except requests.exceptions.RequestException as e:
    print("Error connecting to server:", e)
