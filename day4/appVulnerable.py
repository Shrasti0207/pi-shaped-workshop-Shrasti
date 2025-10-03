from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to vulnerable app!"

@app.route("/insecure")
def insecure():
    user_input = request.args.get("data")
    return str(eval(user_input))  # vulnerable to code injection

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
