from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))

while keyboard.is_pressed('q') == False:
    button = pyautogui.locateOnScreen('heartwp.png', region=(400, 100, 900, 600),
                                      grayscale=True, confidence=0.7)
    if button != None:
        x, y = pyautogui.center(button)
        click(x,y)
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)