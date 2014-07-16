
import cPickle as pickle
import time
import random

with open('words.json', 'rb') as fp:
    word_list = pickle.load(fp)

while True:
    rand_index = random.randint(0, len(word_list))
    item = word_list[rand_index]
    msg =  item["word"] + ": " + item["def"]
    print msg
    time.sleep(5)
