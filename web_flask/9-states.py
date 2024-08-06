#!/usr/bin/python3
"""
This script starts a simple Flask web application.
"""

from flask import Flask, app, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def storage_close(exception):
    """
    This method will close the storage engine when the application is closed.
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Returns a list of all states.
    """
    states = storage.all(State)
    return render_template('9-states.html', states=states)
@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """
    returs all cities associated with a state

    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)