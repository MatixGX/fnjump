import pyautogui as pag
import keyboard
import time

pag.PAUSE = 0.00

count = 2

while True:
    if keyboard.is_pressed(";"):
        print("Ultra jump!!!")
        for i in range(count):
            pag.press("/")
