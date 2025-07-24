from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

HF_API_KEY = os.getenv("HF_API_KEY")
MODEL_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-bn-en"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    input_text = data.get("text", "")

    if not input_text:
        return jsonify({"error": "Text not provided"}), 400

    payload = { "inputs": input_text }

    response = requests.post(MODEL_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        translation = result[0]['translation_text']
        return jsonify({"translation": translation})
    else:
        return jsonify({"error": "Translation failed", "details": response.text}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
