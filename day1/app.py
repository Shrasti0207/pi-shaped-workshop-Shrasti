from flask import Flask
import os

app = Flask(__name__)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

@app.route('/')
def home():
    return f"Hello! Your API_KEY is {AWS_ACCESS_KEY_ID} and SECRET_KEY is {AWS_SECRET_ACCESS_KEY}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
