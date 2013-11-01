#!/usr/bin/python2.7

# Import the modules 
import bitly_api
import random
import json
import ConfigParser as cp
from twython import Twython

class TwitterBot(object):
    #bitly api - shorten url
    def shorten_url(self, a_url, access_token):
        conn = bitly_api.Connection(access_token=access_token)
        data = conn.shorten(a_url)
        shortened_url = data['url']
        return shortened_url
    
    #setup constants from config file
    def send_tweet(self):
        config = cp.ConfigParser()
        config.read("config.ini")
        ACCESS_TOKEN = config.get("BITLY", "ACCESS_TOKEN")
        CONSUMER_KEY = config.get("TWITTER", "CONSUMER_KEY")
        CONSUMER_SECRET = config.get("TWITTER", "CONSUMER_SECRET")
        TOKEN = config.get("TWITTER", "TOKEN")
        TOKEN_SECRET = config.get("TWITTER", "TOKEN_SECRET")
        
        #get word list
        json_data = open('words.json')
        sat_dict = json.load(json_data)
        json_data.close()
        
        #get random word from the word list
        rand_index = random.randint(0, len(sat_dict))
        word = sat_dict[rand_index]['word']
        
        #get shortened url for the definition of the word
        word_url = "http://m.dictionary.com/definition/" + word + "?site=dictwap"
        short_url = self.shorten_url(word_url, ACCESS_TOKEN)
        
        #setup the msg to TWEET
        msg = word + ": " + short_url
        msg += "\n" + "#" + word + " #SAT #satprep #satword"
        
        #tweet message
        twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)
        twitter.update_status(status=msg)
        print(msg)