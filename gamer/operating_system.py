import subprocess
import pyautogui
import time
import math
from gamer.config import Config

DEBUG = True

# Load configuration
config = Config()


class OperatingSystem:

    def press(self, keys, duration=1.0):
        if DEBUG:
            print("[press]")
            print("[press] keys", keys)

        if not isinstance(keys, list):
            keys = [keys]
        try:
            for key in keys:
                pyautogui.keyDown(key)
            time.sleep(duration)
            for key in keys:
                pyautogui.keyUp(key)
        except Exception as e:
            print("[OperatingSystem][press] error:", e)

    def capture_screen(self, file_path):
        subprocess.run(["screencapture", "-C", file_path])
        #subprocess.run(["nircmd.exe", "savescreenshot", file_path])

    
