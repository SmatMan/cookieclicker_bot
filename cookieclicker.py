# this code only really works for me, i'm going to focus on making it automatic in the future

import pyautogui
import time
import keyboard
import upgrades

cookieLocation = (268, 485) # cookie

while True:
    if keyboard.is_pressed('q'):
        break

    if pyautogui.pixel(upgrades.highestPos[0], upgrades.highestPos[1])[1] > 200:
        print("Upgrades Ready")
        upgrades.upgradeAll(upgrades.Upgrades, upgrades.upgradeCount)
        print("Upgrades Completed, Now Clicking...")
    # move cursor to the cookie
    pyautogui.moveTo(cookieLocation[0], cookieLocation[1])
    pyautogui.click(clicks=30, interval=0.001)

    