from apscheduler.scheduler import Scheduler
from twitterbot import TwitterBot

sched = Scheduler()
bot = TwitterBot()

@sched.interval_schedule(minutes=180)
def timed_job():
    print 'This job is run every minute.'
    bot.send_tweet()

sched.start()

while True:
    pass

