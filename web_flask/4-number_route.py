#!/usr/bin/python3
"""
start flask
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Channel Index"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """The /hbnb routing"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """/c routing"""
    return "C %s" % text.replace("_", " ")


@app.route('/python',
           defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """/python channel routing"""
    return "Python %s" % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """/number channel routing"""
    return "%d is a number" % n


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
