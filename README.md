# ⏰ Break Notifier

A simple Python-based break reminder that sends macOS desktop notifications at regular intervals to help you stay focused and healthy while working.

## 💡 Features

- Sends a **“Take a break!”** notification every 50 minutes after script start.
- Sends a **“Break is over!”** notification 10 minutes later.
- Repeats this cycle continuously.
- Runs silently in the background using `nohup`.

## 🖥️ Demo

```bash
Break Time!
🕒 Time to take a break!

...10 minutes later...

Break Over
🚀 Back to work!
```

# 📦 Requirements
- Python 3.7+

- macOS (uses native notification system)

## Install dependencies:
```
pip install notifypy apscheduler
```

# 🚀 Getting Started

1. Clone the Repo

2. Run the Script
```
nohup python3 /full/path/to/break_notifier.py > output.log 2>&1 &

```
3. Stop the Script (When Needed)
Find the process:
```
ps aux | grep break_notifier.py

```
Then stop it:
```
kill <PID>

```

# 🧠 How It Works
This script uses `APScheduler` to:

- Wait 50 minutes after starting.

- Trigger a "Take a break" notification.

- Wait 10 more minutes.

- Trigger a "Break over" notification.

- Repeat this cycle every 60 minutes.

Notifications are sent using `notifypy`, a simple library for native cross-platform notifications.

# 📁 Project Structure
```
break-notifier/
├── break_notifier.py       # Main script
├── output.log              # Runtime log (created automatically)
└── README.md               # You are here
```

# 🎯 Why I Built This
As someone who cares about sustainable productivity and building simple automation tools, I created this script to support healthy work rhythms. It’s also a small demonstration of background scheduling and native macOS notification integration with Python.
