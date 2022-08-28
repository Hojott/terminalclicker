import time
from pynput.keyboard import Controller, Key

keyboard = Controller()

while True:
    keyboard.press(Key.ctrl)
    keyboard.release(Key.ctrl)
    time.sleep(0.001)