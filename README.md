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
ps aux | grep script.py

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

# 🔔 Sound Notifications
By default, this script plays a sound along with the desktop notification using macOS's built-in `afplay` command. This helps you not miss your break — even if you're not looking at the screen.

### 🔉 Changing the Sound
macOS comes with several built-in system sounds located in:
```
/System/Library/Sounds
```
To see available sounds, run this command in y our terminal:
```
ls /System/Library/Sounds
```
You'll get a list like:
```
Basso.aiff  Blow.aiff  Funk.aiff  Ping.aiff  Submarine.aiff  Tink.aiff  ...

```

### ▶️ Test-Playing a Sound
To preview a sound in your terminal:
```
afplay /System/Library/Sounds/Pop.aiff

```
Replace `Pop.aiff` with any other file from the list.

### 🔁 Play All Sounds (One by One)
Use this command (paste it in your terminal) to play each system sound with a short pause between:
```
for sound in /System/Library/Sounds/*.aiff; do
  echo "Playing: $(basename "$sound")"
  afplay "$sound"
  sleep 1
done
```

### 🎯 Changing the Sound in Code
In your break_notifier.py, locate the play_sound() function and update the file path:
```
def play_start_sound():
    subprocess.run(["afplay", "/System/Library/Sounds/Submarine.aiff"])

def play_end_sound():
    subprocess.run(["afplay", "/System/Library/Sounds/Pop.aiff"])
```
