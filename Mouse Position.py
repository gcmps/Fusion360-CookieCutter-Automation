import pyautogui
import time

while True:
    currentMouseX, currentMouseY = pyautogui.position()

    print(currentMouseX, currentMouseY)

    time.sleep(1)