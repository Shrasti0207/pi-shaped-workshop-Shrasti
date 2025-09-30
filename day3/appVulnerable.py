from flask import Flask, request, jsonify, render_template_string
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = '0ff7d16e80eea2593e0c64b661df7cd123456789'


@app.route('/')
def index():
    user = request.args.get('name', '')
    return render_template_string(f"<h1>Hello, My name is Shrasti{user}</h1>")


@app.route('/eval')
def insecure_eval():
    cmd = request.args.get('cmd', '')
    result = eval(cmd)
    return jsonify({'result': str(result)})


@app.route('/secret')
def get_secret():
    return jsonify({'secret': app.config['SECRET_KEY']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)