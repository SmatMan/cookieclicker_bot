# this code only really works for me, i'm going to focus on making it automatic in the future

import pyautogui
import time
import keyboard
import upgrades

cookieLocation = (268, 485) # cookie
upgradeWait = 0

while True:
    if keyboard.is_pressed('q'):
        break

    if upgrades.checkGreen(upgrades.highestPos):
        if upgradeWait == 0:    
            print(f"{upgrades.highest} is ready to upgrade. Waiting {15 - upgradeWait} passes until upgrading to allow more upgrades.")
        if upgradeWait != 15:
            print(f"{15 - upgradeWait}")
            upgradeWait += 1
        else:
            print("Upgrades Ready")
            upgrades.upgradeAll(upgrades.Upgrades, upgrades.upgradeCount)
            print("Upgrades Completed, Now Clicking...")
            upgradeWait = 0

    # move cursor to the cookie
    pyautogui.moveTo(cookieLocation[0], cookieLocation[1])
    pyautogui.click(clicks=50, interval=0.005)

    