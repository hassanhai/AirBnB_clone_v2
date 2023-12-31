#!/usr/bin/python3
<<<<<<< HEAD
"""
starts a Flask web application
=======
"""Start web application with two routings
>>>>>>> e249531fb35d6ac70fb66b24376a91afd3da13da
"""

from flask import Flask, render_template
app = Flask(__name__)


<<<<<<< HEAD
@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
=======
@app.route('/')
def hello():
    """Return string when route queried
    """
>>>>>>> e249531fb35d6ac70fb66b24376a91afd3da13da
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)
=======
    """Return string when route queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Return reformatted text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Reformat text based on optional variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """Allow request if path variable is a valid integer
    """
    return str(n) + ' is a number'
>>>>>>> e249531fb35d6ac70fb66b24376a91afd3da13da

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

web_flask/7-states_list.py

#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)

<<<<<<< HEAD
=======
@app.route('/number_template/<int:n>')
def number_template(n):
    """Retrieve template for request
    """
    path = '5-number.html'
    return render_template(path, n=n)
>>>>>>> e249531fb35d6ac70fb66b24376a91afd3da13da

@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

<<<<<<< HEAD

@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Render template based on conditional
    """
    path = '6-number_odd_or_even.html'
    return render_template(path, n=n)

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
>>>>>>> e249531fb35d6ac70fb66b24376a91afd3da13da
