from flask import Flask, render_template
# render_template() automatically looks for a folder called templates to find the files in the decorators
from .models import DB


def create_app():
    app = Flask(__name__)

    # Add a config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # Connect the database and app
    DB.init_app(app)

    @app.route('/')
    def root():
        return "Welcome Home"

    

    return app