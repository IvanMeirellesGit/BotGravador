import pyautogui
import time

p = pyautogui
def abrirNav():
    p.press('win')
    time.sleep(0.5)
    p.write("twitch.tv/cellbit")
    time.sleep(0.5)
    p.press("Enter")
    time.sleep(12)
    p.press("f")


def abrirOBS():
    p.press('win')
    time.sleep(0.5)
    p.write('obs')