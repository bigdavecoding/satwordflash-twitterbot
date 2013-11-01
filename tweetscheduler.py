from apscheduler.scheduler import Scheduler
from twitterbot import TwitterBot

sched = Scheduler()
bot = TwitterBot()

@sched.interval_schedule(minutes=150)
def timed_job():
    bot.send_tweet()

sched.start()

while True:
    pass

