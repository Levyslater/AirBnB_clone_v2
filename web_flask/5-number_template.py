#!/usr/bin/python3
"""
This script starts a simple Flask web application.
"""

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """
    Home route that returns a simple greeting.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    route returns HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_with_params(text):
    """
    returns 'c' with parameters
    """
    # replace underscore with space
    strip_underscore = text.replace('_', ' ')
    return f'C {strip_underscore}'

@app.route('/python', defaults={'text':' is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_params(text):
    """
    returns 'python' with parameters
    """
    strip_underscore = text.replace('_', ' ')
    return f'Python {strip_underscore}'

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    return f'{n} is a number'
    """
    return f'{n} is a number'
@app.route('/number_template/<int:n>')
def number_template(n):
    """
    render a template with the number passed as a variable
    """

    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
