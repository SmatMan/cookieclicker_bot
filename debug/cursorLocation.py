import pyautogui
import time
import keyboard

# display pixel colur of mouse
'''
while True:
    time.sleep(1)
    pos = pyautogui.position()
    x, y = pos.x, pos.y
    print(pyautogui.pixel(x, y))
'''
# same but check if the pixel is green
while True:
    time.sleep(1)
    pos = pyautogui.position()
    x, y = pos.x, pos.y
    #if pyautogui.pixel(x, y)[1] > 200:
    print(f"({x}, {y}) = {pyautogui.pixel(x, y)}")
