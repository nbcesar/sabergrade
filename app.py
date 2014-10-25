from flask import Flask
from flask import request, render_template, flash, url_for, redirect
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()