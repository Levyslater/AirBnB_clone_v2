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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
