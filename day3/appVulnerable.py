from flask import Flask, request, jsonify, render_template_string
import os


app = Flask(__name__)


# INTENTIONAL: hardcoded secret for the exercise
app.config['SECRET_KEY'] = 'hardcoded_secret_12345'


@app.route('/')
def index():
    user = request.args.get('name', '')
    # INTENTIONAL: unsafe rendering (reflective XSS)
    return render_template_string(f"<h1>Hello, My name is Shrasti{user}</h1>")


@app.route('/eval')
def insecure_eval():
    cmd = request.args.get('cmd', '')
    # INTENTIONAL: dangerous use of eval()
    result = eval(cmd)
    return jsonify({'result': str(result)})


@app.route('/secret')
def get_secret():
    # returns the hardcoded secret (to be detected by gitleaks)
    return jsonify({'secret': app.config['SECRET_KEY']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)