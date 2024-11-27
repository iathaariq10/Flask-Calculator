from flask import Flask, render_template, request
import math

app = Flask(__name__)

history = []

def evaluate_expression(expression):
    try:
        expression = expression.replace('÷', '/').replace('x', '*')

        expression = ''.join(
            [char + '*' if char.isdigit() and i + 1 < len(expression) and expression[i + 1] == '(' else char
             for i, char in enumerate(expression)]
        )
        expression = expression.replace(')(', ')*(')

        if '%' in expression:
            expression = expression.replace('%', '/100')

        allowed_chars = "0123456789+-*/.()%"
        if all(c in allowed_chars for c in expression):
            result = eval(expression)
            return result
        else:
            return "Error: Invalid characters in expression"
    except Exception as e:
        return f"Error: {e}"


@app.route('/', methods=['GET', 'POST'])
def index():
    global history
    result = ''

    if request.method == 'POST':
        expression = request.form.get('expression', '')

        if expression and expression != 'clear':
            result = evaluate_expression(expression)
            history.append(f"{expression} = {result}")
        elif expression == 'clear':
            history = []

    return render_template('index.html', result=result, history=history)


if __name__ == '__main__':
    app.run(debug=True)