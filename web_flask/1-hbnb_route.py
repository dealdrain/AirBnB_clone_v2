#!/usr/bin/python3
"""
flask in
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """the channel index"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Channel /hbnb"""
    return "HBNB"


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
