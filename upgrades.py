from enum import Enum
import pyautogui
import time 

class Upgrades(Enum):
    SHIPMENT = (1679, 853)
    WIZARD = (1685, 785)
    TEMPLE = (1678, 722)
    BANK = (1678, 659)
    FACTORY = (1676, 597)

order = [name for name, member in Upgrades.__members__.items()]
highest = order[0]
print(f"{highest} is the highest current upgrade")
highestPos = getattr(Upgrades, highest).value
upgradeCount = len(order)

def checkGreen(pos):
    for i in range(10):
        if pyautogui.pixel(pos[0] - i, pos[1])[1] > 200:
            return True
    for i in range(10):
        if pyautogui.pixel(pos[0] + i, pos[1])[1] > 200:
            return True
    return False

def upgradeAll(Upgrades, upgradeCount):
    for i in range(upgradeCount):
        toUpgrade = order[i]
        toUpgradePos = getattr(Upgrades, toUpgrade).value
        while checkGreen(toUpgradePos):
            print(f"{toUpgrade} is ready to upgrade")
            pyautogui.moveTo(toUpgradePos[0], toUpgradePos[1])
            pyautogui.click()
            time.sleep(0.5)
    print("Upgrades finished.")
