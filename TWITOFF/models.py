""" Database models """

from flask_sqlalchemy import SQLAlchemy



# Import database (CAPS for global scope)
DB = SQLAlchemy()

class User(DB.Model):
    """ Twitter users that we analize """
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

class Tweet(DB.Model):
    """ The users tweets from twitter """
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))
    