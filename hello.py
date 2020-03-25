"""MINIMAL FLASK APP"""

from flask import Flask

# Make the application
app = Flask(__name__)

# Make the rout
@app.route("/")

def hello():
    return "Hello!"