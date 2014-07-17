from apscheduler.scheduler import Scheduler
from twitterbot import TwitterBot
import time

sched = Scheduler()
bot = TwitterBot()
bot.send_tweet()

@sched.interval_schedule(minutes=120)
def timed_job():
    bot.send_tweet()

sched.start()

while True:
    time.sleep(1)

