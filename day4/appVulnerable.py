from flask import Flask, request, jsonify
import os

app = Flask(__name__)

#fake secret key
AWS_SECRET_ACCESS_KEY = "0ff7d16e80eea2593e0c64b661df7cd1856g4dsf"

@app.route('/')
def home():
    return f"Hello! Your SECRET_KEY is {AWS_SECRET_ACCESS_KEY}"

@app.route('/eval') 
def insecure_eval(): 
    cmd = request.args.get('cmd', '') 
    result = eval(cmd) 
    return jsonify({'result': str(result)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)