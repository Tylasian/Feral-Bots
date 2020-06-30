from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

pyautogui.FAILSAFE = True

#coords x,y
GrabTable = 630,900

BottomTable = 1020,720
BottomIn = 930,635
BottomTOut = 1020,545

TopTable = 1020,380
TopIn = 935,320
TopOut = 1095,315

MiddleTable = 930,460
MiddleIn = 850,560
MiddleOut = 1020,560

TableRot = 1690,285
TableFlip =  1620,285


def click(x):
    win32api.SetCursorPos((x))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def holdMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)

def releaseMouse():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.5)
    
def grabTable():
    win32api.SetCursorPos((GrabTable))
    holdMouse()
    time.sleep(.5)

def rotate():
    click((TableRot))
    time.sleep(.5)

def flip():
    click(TableFlip)
    time.sleep(.5)
    
def goToBottomIn():
    win32api.SetCursorPos(BottomIn)
    time.sleep(.5)
    
def goToBottomOut():
    win32api.SetCursorPos(BottomOut)
    time.sleep(.5)
    
def goToMiddleIn():
    win32api.SetCursorPos(MiddleIn)
    time.sleep(.5)
    
def goToMiddleOut():
    win32api.SetCursorPos(MiddleOut)
    time.sleep(.5)
    
def goToTopIn():
    win32api.SetCursorPos(TopIn)
    time.sleep(.5)
    
def goToTopOut():
    win32api.SetCursorPos(TopOut)
    time.sleep(.5)

def travel(horiz,vert):
    x,y = pyautogui.position()
    pyautogui.moveTo(x + horiz,y + vert)

# vvv wow yeet the instructions into here vvv
while keyboard.is_pressed('q') == False: #hold 'q' to stop loop
    grabTable()
    pyautogui.moveTo(BottomTable)
    releaseMouse()
    grabTable()
    pyautogui.moveTo(TopTable)
    releaseMouse()
    grabTable()
    pyautogui.moveTo(MiddleTable)
    releaseMouse()
    rotate()
    rotate()
    flip()
    goToMiddleIn()
    travel(100,100)
    
