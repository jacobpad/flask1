import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User
from .twitter import BASILICA


def predict_user(user1_name, user2_name, tweet_text, cache=None):
    """ Figure out which user is more likely to say a given phrase & return the user """

    user_set = pickle.dumps((user1_name, user2_name))

    if cache and cache.exists(user_set):
        log_reg = pickle.loads(cache.get(user_set))
    else:
        # Get users
        user1 = User.query.filter(User.name == user1_name).one()
        user2 = User.query.filter(User.name == user2_name).one()

        # Embeddings
        user1_embeds = np.array([tweet.embedding for tweet in user1.tweets])
        user2_embeds = np.array([tweet.embedding for tweet in user2.tweets])

        # Split into array
        embeddings = np.vstack([user1_embeds, user2_embeds])

        # Labels
        labels = np.concatenate([np.ones(len(user1.tweets)),
                                 np.zeros(len(user2.tweets))])

        # Fit the Logistic Regression model
        log_reg = LogisticRegression().fit(embeddings, labels)

        # Optional
        cache and cache.set(user_set, pickle.dumps(log_reg))

    # Use BASILICA to run the embeddings
    tweet_embedding = BASILICA.embed_sentence(tweet_text, model='twitter')

    return log_reg.predict(np.array(tweet_embedding).reshape(1, -1))