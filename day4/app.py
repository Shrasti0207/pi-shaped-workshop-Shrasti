from flask import Flask, request, jsonify
import os

app = Flask(__name__)

#fake secret key
AWS_SECRET_ACCESS_KEY = "0ff7d16e80eea2593e0c64b661df7cd1856g4dsf"

@app.route('/')
def home():
    return f"Hello! Your SECRET_KEY is {AWS_SECRET_ACCESS_KEY}"

@app.route("/insecure")
def insecure():
    user_input = request.args.get("data")
    return str(eval(user_input))  # vulnerable to code injection

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
