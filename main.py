"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
from flask import request, render_template, flash, url_for, redirect
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/thegrid')
def thegrid():
	return render_template('thegrid.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
