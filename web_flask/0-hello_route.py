#!/usr/bin/python3
""" A module serves as a flask starter """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """A function that serves as the home route of the application.
    Returns:
        str: The greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
