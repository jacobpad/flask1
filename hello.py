# FLASK_APP=hello.py flask run
"""MINIMAL FLASK APP"""

from flask import Flask, render_template
# render_template() automatically looks for a folder called templates to find the files in the decorators

# Make the application
app = Flask(__name__)

# Make the rout and function for home page
@app.route("/")
def hello():
    return render_template('home.html')

# Make out and functionn for about page
@app.route("/about")
def about_page():
    return render_template('about.html')
    