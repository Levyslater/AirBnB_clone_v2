#!/usr/bin/python3
"""
This script starts a simple Flask web application.
"""

from flask import Flask

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
    replace underscore with space
    strip_underscore = text.replace('_', ' ')
    return f'C {strip_underscore}'
    """
    # replace underscore with space
    strip_underscore = text.replace('_', ' ')
    return f'C {strip_underscore}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
