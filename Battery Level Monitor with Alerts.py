import psutil
from plyer import notification
import time

def check_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged

    if percent >= 90 and plugged:
        notification.notify(
            title="Battery Status 🔌",
            message="Unplug, save your battery life! 🔋",
            timeout=5
        )
    elif percent <= 20 and not plugged:
        notification.notify(
            title="Battery Status ⚠️",
            message="Bro, charge that thing 😬",
            timeout=5
        )
    else:
        print(f"Battery level: {percent}%. All good 👌")

# Runs every 60 seconds
while True:
    check_battery()
    time.sleep(60)
