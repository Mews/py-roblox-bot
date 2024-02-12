import pydirectinput as dinput
from time import sleep as wait
from pygetwindow import getWindowsWithTitle, getActiveWindow
from win32gui import GetWindowText, GetForegroundWindow
import pyperclip as pyclip
from .exceptions import *

UI_NAV_ENABLED = False

def require_focus(fn):
    #Fast check to see if roblox window is already focused
    if GetWindowText(GetForegroundWindow()) == "Roblox":
        return fn

    else:
        rblxWindow = None

        #Find roblox window
        for window in getWindowsWithTitle("Roblox"):
            if window.title == "Roblox":
                rblxWindow = window
        
        #Raise error if roblox isn't open
        if rblxWindow == None:
            raise NoRobloxWindowException("You must have roblox opened")
        
        #Set focus to roblox window
        else:
            rblxWindow.maximize()
            rblxWindow.activate()

            #Wait for the roblox window to be active
            while getActiveWindow() == None:
                pass
                
        return fn

@require_focus
def keyboard_action(action:float):
    dinput.press(action)

@require_focus
def hold_keyboard_action(action:str, duration:float):
    dinput.keyDown(action)
    wait(duration)
    dinput.keyUp(action)

def walk(direction:str, duration:float):
    direction = direction.lower().strip()

    forwardDirections = ["f", "fw", "forward", "forwards"]
    leftDirections = ["l", "left"]
    rightDirections = ["r", "right"]
    backDirections = ["b", "back", "backward", "backwards"]

    if direction in forwardDirections:
        walk_forward(duration)
    
    elif direction in leftDirections:
        walk_left(duration)
    
    elif direction in rightDirections:
        walk_right(duration)
    
    elif direction in backDirections:
        walk_back(duration)
    
    else:
        excTxt = "Direction must be one of these: "
        for d in forwardDirections: excTxt += d + " "
        for d in leftDirections: excTxt += d + " "
        for d in rightDirections: excTxt += d + " "
        for d in backDirections: excTxt += d + " "
        raise InvalidWalkDirectionException(excTxt)

@require_focus
def walk_forward(duration:float):
    dinput.keyDown("w")
    wait(duration)
    dinput.keyUp("w")

@require_focus
def walk_left(duration:float):
    dinput.keyDown("a")
    wait(duration)
    dinput.keyUp("a")

@require_focus
def walk_right(duration:float):
    dinput.keyDown("d")
    wait(duration)
    dinput.keyUp("d")

@require_focus
def walk_back(duration:float):
    dinput.keyDown("s")
    wait(duration)
    dinput.keyUp("s")

@require_focus
def jump(number_of_jumps:int=1, delay:float=0):
    for i in range(number_of_jumps):
        dinput.press("space")
        wait(delay)

@require_focus
def jump_continuous(duration:float):
    dinput.keyDown("space")
    wait(duration)
    dinput.keyUp("space")

@require_focus
def reset_player(interval:float=0.5):
    dinput.press(("esc", "r", "enter"), interval=interval)

@require_focus
def leave_game(interval:float=0.5):
    dinput.press(("esc", "l", "enter"), interval=interval)

@require_focus
def toggle_shift_lock():
    dinput.press("shift")

@require_focus
def chat(message:str):
    #Open chat
    dinput.keyDown("shift")
    dinput.keyDown("7")
    dinput.keyUp("shift")
    dinput.keyUp("7")

    #Use clipboard to paste message quickly
    previousClipboard = pyclip.paste()

    pyclip.copy(message)
    dinput.keyDown("ctrl")
    dinput.keyDown("v")
    dinput.keyUp("ctrl")
    dinput.keyUp("v")

    dinput.press("enter")

    toggle_shift_lock()

    #Restore previous clipboard content
    pyclip.copy(previousClipboard)

@require_focus
def toggle_ui_navigation():
    global UI_NAV_ENABLED
    UI_NAV_ENABLED = not UI_NAV_ENABLED
    dinput.press('`')

@require_focus
def ui_navigate_up():
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press('up')

@require_focus
def ui_navigate_left():
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press('left')

@require_focus
def ui_navigate_right():
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press('right')

@require_focus
def ui_navigate_down():
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press('down')

@require_focus
def ui_click():
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press("enter")

@require_focus
def equip_slot(slot:int):
    if slot < 0 or slot > 9:
        raise InvalidSlotNumberException("Slots should be between 0 and 9")

    dinput.press(str(slot))