#!/usr/bin/python3
"""
start Flask
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Starting Flask"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Add route /hbnb"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text=None):
    """ inputed str 'replace _ for space and show text'"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is_cool'):
    """input text 'replace _ for space and show text'"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
