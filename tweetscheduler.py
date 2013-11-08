from apscheduler.scheduler import Scheduler
from twitterbot import TwitterBot
import time

sched = Scheduler()
bot = TwitterBot()

@sched.interval_schedule(minutes=150)
def timed_job():
    bot.send_tweet()

sched.start()

while True:
    time.sleep(1)

