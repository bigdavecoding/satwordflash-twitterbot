from apscheduler.scheduler import Scheduler
from twitterbot import TwitterBot

sched = Scheduler()
bot = TwitterBot()

@sched.interval_schedule(minutes=1)
def timed_job():
    print 'This job is run every minute.'
    bot.send_tweet()

@sched.cron_schedule(day_of_week='mon-fri', hour=17)
def scheduled_job():
    print 'This job is run every weekday at 5pm.'

sched.start()

while True:
    pass

