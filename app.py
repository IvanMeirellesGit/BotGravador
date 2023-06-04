import pyautogui
import time

p = pyautogui


def abrirNav():
    p.press('win')
    p.write("Edge")
    p.press("Enter")


abrirNav()
