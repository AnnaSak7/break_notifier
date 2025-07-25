from notifypy import Notify
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
import time
import subprocess

def play_start_sound():
    subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])

def play_end_sound():
    subprocess.run(["afplay", "/System/Library/Sounds/Hero.aiff"])

def notify_break_start():
    notification = Notify()
    notification.title = "Break Time!"
    notification.message = "🕒　Time to take a break!"
    notification.send()
    play_start_sound()

def notify_break_end():
    notification = Notify()
    notification.title = "Break Over!"
    notification.message = "🚀　Back to work!"
    notification.send()
    play_end_sound()
    
def schedule_break_cycle():
    notify_break_start()
    
    # Schedule the end of break in 10 minutes
    scheduler.add_job(
        notify_break_end,
        trigger="date",
        run_date=datetime.now() + timedelta(minutes=1)
    )

scheduler = BlockingScheduler()
scheduler.add_job(
    schedule_break_cycle,
    "interval",
    minutes=2,
    next_run_time=datetime.now() + timedelta(minutes=1),
    id="break_notification_job"
) 

scheduler.start()

try: 
    while True:
        time.sleep(1)
except(KeyboardInterrupt, SystemExit):
    scheduler.shutdown