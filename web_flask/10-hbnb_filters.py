#!/usr/bin/python3
"""
This script starts a simple Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)

@app.teardown_appcontext
def storage_close(exception):
    """
    This method will close the storage engine when the application is closed.
    """
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Display a HTML page like 6-index.html, with States, Cities, and Amenities
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
                                                                                                                                      