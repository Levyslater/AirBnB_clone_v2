#!/usr/bin/python3
"""
This script starts a simple Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def index():
    """
    Home route that returns a simple greeting.
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
