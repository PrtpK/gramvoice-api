from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "GramVoice API is live and working!"

@app.route("/hello")
def hello():
    return "Hello from GramVoice API!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
