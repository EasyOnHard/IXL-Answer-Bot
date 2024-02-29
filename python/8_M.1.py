import pyautogui
import time
import keyboard
from sys import exit

def screen_cord(percent, screen):
    return round(percent / 100 * screen)

screenx,screeny = pyautogui.size()
screenx,screeny=int(str(screenx)),int(str(screeny))

question_x1 = screen_cord(36, screenx)
question_x2 = screen_cord(47, screenx)
question_y = screen_cord(46, screeny)
question_incomplete_x = screen_cord(61, screenx)
question_incomplete_y = screen_cord(49, screeny)
question_answer_x = screen_cord(66, screenx)

def mouse_pos():                # Prints The Position of the Mouse
    print(pyautogui.position())

def test_macro():               # Runs the Macro One Time
    time.sleep(0.35)
    pyautogui.click(question_x1, question_y)
    time.sleep(0.01)
    pyautogui.click(question_x2, question_y)
    time.sleep(0.01)
    pyautogui.press('enter')
    time.sleep(0.9)
    pyautogui.click(question_incomplete_x, question_incomplete_y)
    for i in range(5):
        y = i * 25 + 640
        pyautogui.click(question_answer_x, y)

def infinite_macro():          # Runs test_macro 
    while True:
        test_macro()
        if keyboard.is_pressed('ctrl + y'):
            break

print("+----------------------------------+")
print("| Ctrl + M: Get Mouse Position     |")
print("| Ctrl + T: Test Macro             |")
print("| Ctrl + I: Loop Macro             |")
print("| Ctrl + Y (Hold): Break from Loop |")
print("| Ctrl + Y + Esc: Exit             |")
print("+----------------------------------+")
print(f"Monitor Size: ({screenx}, {screeny})")

keyboard.add_hotkey('ctrl + m', lambda: mouse_pos())      # Hotkey for mouse_pos()
keyboard.add_hotkey('ctrl + t', lambda: test_macro())     # Hotkey for test_macro()
keyboard.add_hotkey('ctrl + i', lambda: infinite_macro()) # Hotkey for infinite_macro() 

keyboard.wait('esc')           # Keeps program on until Escape is hit
