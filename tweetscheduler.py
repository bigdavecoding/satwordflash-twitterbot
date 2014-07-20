from apscheduler.scheduler import Scheduler
from twitterbot import TwitterBot
import time
from app_config import AppConfig

sched = Scheduler()
config = AppConfig()
bot = TwitterBot(config)
bot.send_tweet()

@sched.interval_schedule(minutes=120)
def timed_job():
    bot.send_tweet()

sched.start()

while True:
    time.sleep(1)
