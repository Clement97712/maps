from apscheduler.schedulers.blocking import BlockingScheduler
import time
import logging
sched = BlockingScheduler()
logging.basicConfig(level=logging.DEBUG)


@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print(time.time)
    print('This job is run every three minutes.')


sched.start()
