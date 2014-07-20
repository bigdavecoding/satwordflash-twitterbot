import os
import base64

class AppConfig(object):

    def __init__(self):
        #setup constants from environment variables
        self.access_token = os.environ.get("ACCESS_TOKEN")
        self.consumer_key = os.environ.get("CONSUMER_KEY")
        self.consumer_secret = os.environ.get("CONSUMER_SECRET")
        self.token = os.environ.get("TOKEN")
        self.token_secret = os.environ.get("TOKEN_SECRET")
        self.mongo_url = base64.b64decode(os.environ.get("URL")).decode('ascii')
        self.mongo_db = os.environ.get("DATABASE")
        self.mongo_user = base64.b64decode(os.environ.get("USERNAME")).decode('ascii')
        self.mongo_pass = base64.b64decode(os.environ.get("PASSWORD")).decode('ascii')

    def __str__(self):
        str_rep = "ACCESS TOKEN: " + self.access_token
        str_rep += "CONSUMER KEY: " + self.consumer_key
        str_rep += "CONSUMER SECRET: " + self.consumer_secret
        str_rep += "TOKEN: " + self.token
        str_rep += "TOKEN SECRET: " + self.token_secret
        str_rep += "MONGO URL: " + self.mongo_url
        str_rep += "MONGO DB: " + self.mongo_db
        str_rep += "MONGO USER: " + self.mongo_user
        str_rep += "MONGO PASS: " + self.mongo_pass
        return str_rep