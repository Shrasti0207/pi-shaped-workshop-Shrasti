from flask import Flask, request, abort
import ast
import operator as op
import os

app = Flask(__name__)

# allowed operators
_ops = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
}

def safe_eval(expr: str):
    """
    Evaluate arithmetic expressions containing numbers, + - * / %, //, ** and parentheses.
    Raises ValueError for invalid/unsafe expressions.
    """
    try:
        node = ast.parse(expr, mode='eval').body
    except Exception as e:
        raise ValueError("Invalid expression")

    def _eval(node):
        if isinstance(node, ast.Constant):  # python3.8+: numbers are Constant
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Only numbers allowed")
        if isinstance(node, ast.Num):  # for older Python
            return node.n
        if isinstance(node, ast.BinOp):
            left = _eval(node.left)
            right = _eval(node.right)
            op_type = type(node.op)
            if op_type in _ops:
                return _ops[op_type](left, right)
            raise ValueError("Operator not allowed")
        if isinstance(node, ast.UnaryOp):
            operand = _eval(node.operand)
            op_type = type(node.op)
            if op_type in _ops:
                return _ops[op_type](operand)
            raise ValueError("Unary operator not allowed")
        raise ValueError("Expression type not allowed")

    result = _eval(node)
    return result

@app.route("/")
def home():
    return "Welcome to vulnerable application."

@app.route("/insecure")
def insecure():
    user_input = request.args.get("data", "")
    if not user_input:
        return "Provide ?data=<expression>"
    # limit length to avoid abuse
    if len(user_input) > 200:
        abort(400, "Expression too long")
    try:
        val = safe_eval(user_input)
        return str(val)
    except ValueError as e:
        abort(400, str(e))

if __name__ == "__main__":
    # turn off debug for CI/production; enable only for local debugging
    debug_mode = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
