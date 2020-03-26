from flask import Flask, render_template
# render_template() automatically looks for a folder called templates to find the files in the decorators
from .models import DB, User
from decouple import config

def create_app():
    app = Flask(__name__)

    # Add a config
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #This code removes an error
    # In terminal: CREATE DATABASE by running 
    # FLASK_APP=TWITOFF:APP flask shell
    # from TWITOFF.models import *
    # DB.create_all()      ################# WHERE DID CREATE ALL COME FROM???? ##################
                           ################# https://youtu.be/WgING5oXNKA?t=6216 #################
    # quit()



    # Create users within the flask shell
    # Open shell:
    # FLASK_APP=TWITOFF:APP flask shell
    # from TWITOFF.models import *
    # u1 = User(name='austen') #See user class in models.py
    # t1 = Tweet(text='wa-hoo!!!!') #See user class in models.py
    # DB.session.add(u1)
    # DB.session.add(t1)
    # DB.session.commit()
    # quit()


    # DB.drop_all()     #Drops all tables from the database
    # DB.create_all()   #Creates the tables in the database


    # Connect the database and app
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Rest Database', users=[])

        # 
        # Add to database
        # 
        # FLASK_APP=TWITOFF:APP flask shell
        # from TWITOFF.models import *
        # DB.drop_all()
        # DB.create_all()
        # twitter_user = TWITTER.get_user('DatingDivas')
        # tweets = twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, tweet_mode='extended')
        # db_user=User(id=twitter_user.id, name=twitter_user.screen_name, newest_tweet_id=tweets[0].id)
        # 
        # >>> for tweet in tweets:
        # ...   embedding = BASILICA.embed_sentence(tweet.full_text, model='twitter')
        # ...   db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:500], embedding=embedding)
        # ...   DB.session.add(db_tweet)
        # ...   db_user.tweets.append(db_tweet)
        # 
        # DB.session.add(db_user)
        # DB.session.commit()
        # quit()
        # 
        # EXPLAINED: https://youtu.be/2YE6jcy-chg?t=7007


    return app