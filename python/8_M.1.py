import pyautogui
import time
import keyboard
from sys import exit

def mousepos():
    print(pyautogui.position())

def test_macro():
    time.sleep(0.35)
    pyautogui.click(700, 500)
    time.sleep(0.01)
    pyautogui.click(900, 500)
    time.sleep(0.01)
    pyautogui.press('enter')
    time.sleep(0.9)
    pyautogui.click(1170, 530)
    time.sleep(0.01)
    pyautogui.click(1220, 660)
    time.sleep(0.01)
    pyautogui.click(1220, 715)
    time.sleep(0.01)
    pyautogui.click(1220, 745)

def infinite_macro():
    while True:
        time.sleep(0.35)
        pyautogui.click(700, 500)
        time.sleep(0.01)
        pyautogui.click(900, 500)
        time.sleep(0.01)
        pyautogui.press('enter')
        time.sleep(0.9)
        pyautogui.click(1170, 530)
        for i in range(7):
            y = i * 20 + 600
            pyautogui.click(1220,y)
        if keyboard.is_pressed('ctrl + y'):
            break

keyboard.add_hotkey('ctrl + m', lambda: mousepos())
keyboard.add_hotkey('ctrl + t', lambda: test_macro())
keyboard.add_hotkey('ctrl + i', lambda: infinite_macro())

keyboard.wait('esc')