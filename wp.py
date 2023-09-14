import ctypes
import os
import time

# Get the absolute path of the initial wallpaper
absPath = os.path.abspath("./indir.png")

def ChangeWp(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

# Function to check if the wallpaper has changed
def wallpaper_changed(last_path):
    current_path = ctypes.create_unicode_buffer(260)  # Buffer to hold the current wallpaper path
    ctypes.windll.user32.SystemParametersInfoW(20, 260, current_path, 0)  # Get the current wallpaper path
    return current_path.value != last_path

if __name__ == "__main__":
    last_wallpaper = absPath  # Initial wallpaper path
    
    while True:
        if wallpaper_changed(last_wallpaper):
            last_wallpaper = ctypes.create_unicode_buffer(260)  # Update the last wallpaper path
            ctypes.windll.user32.SystemParametersInfoW(20, 260, last_wallpaper, 0)  # Get the current wallpaper path
            ChangeWp(absPath)
        
        # Poll every 1 second (adjust as needed)
        time.sleep(1)
