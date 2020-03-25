"""ENTRY POINT FOR FLASK APP"""
from .app import create_app


APP = create_app() # APP is a global variable

# Run this in the terminal with FLASK_APP=TWITOFF:APP flask run