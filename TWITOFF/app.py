from flask import Flask, render_template
# render_template() automatically looks for a folder called templates to find the files in the decorators

def create_app():
    app = Flask(__name__)

    @app.rout('/')
    def root():
        return "Welcome Home"

    

    return app