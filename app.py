import sys
import os
import threading
import tkinter as tk
from tkinter import PhotoImage

# Add the 'modules' folder to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from modules.EVA import EVA
from modules.FileManager import read_json_key

path_eva = 'files/eva.json'     # File path for status

# GUI Function to update the status
def update_status_label():
    try:
        status = read_json_key(path_eva, 'status')
        if status == 'listening':
            window.title("Listening")
            window.iconphoto(False, PhotoImage(file="interface/circle_green.png"))
        elif status == 'recognizing':
            window.title("Recognizing")
            window.iconphoto(False, PhotoImage(file="interface/circle_yellow.png"))
        elif status == 'processing':
            window.title("Processing")
            window.iconphoto(False, PhotoImage(file="interface/circle_blue.png"))
        elif status == 'speaking':
            window.title("Speaking")
            window.iconphoto(False, PhotoImage(file="interface/circle_purple.png"))
        else:
            window.title("Terminated")
            window.iconphoto(False, PhotoImage(file="interface/circle_red.png")) 
    except Exception as e:
        print(f"Error reading status file: {e}")

    # Schedule the function to update every 1 ms
    window.after(1, update_status_label)

# Function to run EVA in the background
def run_eva_in_background():
    EVA()


# Create the main window
window = tk.Tk()
window.title("EVA")
window.geometry("300x0")

# To prevent the window from being closed or disappearing when clicking outside
window.attributes("-topmost", True)  # Keep the window on top
window.grab_set()  # Make the window grab all events (focus, clicks, etc.)

# Start a thread to run the EVA function in the background
eva_thread = threading.Thread(target=run_eva_in_background, daemon=True)
eva_thread.start()

# Start the status update loop
update_status_label()

# Start the Tkinter event loop
window.mainloop()
