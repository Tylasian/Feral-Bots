from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import sys
pyautogui.FAILSAFE = True

#coords x,y

Drop = 943,593
Mix = 620,860
Top = 711,223
Bottom = 720,492
PlayAg = 726,834

def click(x):
    win32api.SetCursorPos((x))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def holdMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)

def releaseMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.5)

def travel(horiz,vert):
    x,y = pyautogui.position()
    pyautogui.moveTo(x + horiz,y + vert)

# vvv wow yeet the instructions into here vvv

    
while keyboard.is_pressed('q') == False: #hold 'q' to stop loop
        
    click(Top)
    time.sleep(.5)
    click(Drop)
    time.sleep(.5)
    click(Top)
    time.sleep(.5)
    click(Drop)
    time.sleep(.5)

    click(Mix)
    time.sleep(1)

    click(Drop)
    time.sleep(.5)
    click(Top)
    time.sleep(.5)
    click(Drop)
    time.sleep(.5)
    click(Drop)
    time.sleep(1)
    
    click(PlayAg)
    time.sleep(1)

    
    
    
