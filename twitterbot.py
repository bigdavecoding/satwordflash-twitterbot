#!/usr/bin/python2.7

# Import the modules 
import bitly_api
import random
import cPickle as pickle
from twython import Twython
from pymongo import MongoClient

class TwitterBot(object):

    def __init__(self, config):
        self.config = config

        #get word list
        with open('words.pickle', 'rb') as fp:
            self.word_list = pickle.load(fp)

    #bitly api - shorten url
    def shorten_url(self, a_url, access_token):
        conn = bitly_api.Connection(access_token=access_token)
        data = conn.shorten(a_url)
        shortened_url = data['url']
        return shortened_url

    def log_word(self, word):
        mongo_client = MongoClient(self.config.mongo_url)
        db = mongo_client[self.config.mongo_db]
        db.authenticate(self.config.mongo_user, self.config.mongo_pass)
        word_activity_log = db["word_activity"]
        word_activity_log.insert({"word": word})

    def send_tweet(self):        
        #get random word from the word list
        rand_index = random.randint(0, len(self.word_list))
        word = self.word_list[rand_index]['word']
        a_def = self.word_list[rand_index]['def']
        
        #get shortened url for the definition of the word
        word_url = "http://m.dictionary.com/definition/" + word + "?site=dictwap"
        short_url = self.shorten_url(word_url, self.config.access_token)
        
        #setup the msg to TWEET
        msg = word + ": " + a_def
        msg += " " + short_url
        msg += "\n" + "#" + word + " #SAT"
        
        #tweet message
        twitter = Twython(self.config.consumer_key, self.config.consumer_secret, self.config.token, self.config.token_secret)
        twitter.update_status(status=msg)
        self.log_word(word)
        print(msg)