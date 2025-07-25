from notifypy import Notify
from apscheduler.schedulers.blocking import BlockingScheduler
import time

def notify_break_start():
    notification = Notify()
    notification.title = "Break Time!"
    notification.message = "Time to take a break!"
    notification.send()

def notify_break_end():
    notification = Notify()
    notification.title = "Break Over!"
    notification.message = "Back to work!"
    notification.send()
    
def schedule_break_cycle():
    notify_break_start()
    
    scheduler.add_job(
        notify_break_end,
        trigger="date",
        run_date=time.time() + 600
    )

scheduler = BlockingScheduler()
scheduler.add_job(
    schedule_break_cycle,
    "interval",
    minutes=60,
    next_run_time=time.time() + 3000, # 50 min = 3000 sec
    id="break_notification_job"
) 

scheduler.start()

try: 
    while True:
        time.sleep(1)
except(KeyboardInterrupt, SystemExit):
    scheduler.shutdown