#!/usr/bin/python2.7

# Import the modules 
import bitly_api
import random
import json
import ConfigParser as cp
from twython import Twython

class TwitterBot(object):

    def __init__(self):
        #get word list        
        json_data = open("words.json")
        self.word_list = json.load(json_data)
        json_data.close()
        
        #setup constants from config file
        config = cp.ConfigParser()
        config.read("config.ini")
        self.access_token = config.get("BITLY", "ACCESS_TOKEN")
        self.consumer_key = config.get("TWITTER", "CONSUMER_KEY")
        self.consumer_secret = config.get("TWITTER", "CONSUMER_SECRET")
        self.token = config.get("TWITTER", "TOKEN")
        self.token_secret = config.get("TWITTER", "TOKEN_SECRET")        
    
    #bitly api - shorten url
    def shorten_url(self, a_url, access_token):
        conn = bitly_api.Connection(access_token=access_token)
        data = conn.shorten(a_url)
        shortened_url = data['url']
        return shortened_url
        
    def send_tweet(self):        
        #get random word from the word list
        rand_index = random.randint(0, len(self.word_list))
        word = self.word_list[rand_index]['word']
        
        #get shortened url for the definition of the word
        word_url = "http://m.dictionary.com/definition/" + word + "?site=dictwap"
        short_url = self.shorten_url(word_url, self.access_token)
        
        #setup the msg to TWEET
        msg = word + ": " + short_url
        msg += "\n" + "#" + word + " #SAT #satprep #satword"
        
        #tweet message
        twitter = Twython(self.consumer_key, self.consumer_secret, self.token, self.token_secret)
        twitter.update_status(status=msg)
        print(msg)