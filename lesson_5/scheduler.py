from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()


def some_job():
    print('Every 10 seconds')


sched.add_job(some_job, 'interval', seconds=1)
sched.start()

while True:
    pass
