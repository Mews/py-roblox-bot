import pydirectinput as dinput
from time import sleep as wait
from pygetwindow import getWindowsWithTitle, getActiveWindow
from win32gui import GetWindowText, GetForegroundWindow
import pyperclip as pyclip

UI_NAV_ENABLED = False

class NoRobloxWindowException(Exception):
    pass

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
def keyboard_action(action):
    dinput.press(action)

@require_focus
def hold_keyboard_action(action, duration):
    dinput.keyDown(action)
    wait(duration)
    dinput.keyUp(action)

@require_focus
def walk_forward(duration):
    dinput.keyDown("w")
    wait(duration)
    dinput.keyUp("w")

@require_focus
def walk_left(duration):
    dinput.keyDown("a")
    wait(duration)
    dinput.keyUp("a")

@require_focus
def walk_right(duration):
    dinput.keyDown("d")
    wait(duration)
    dinput.keyUp("d")

@require_focus
def walk_back(duration):
    dinput.keyDown("s")
    wait(duration)
    dinput.keyUp("s")

@require_focus
def jump(number_of_jumps=1, delay=0):
    for i in range(number_of_jumps):
        dinput.press("space")
        wait(delay)

@require_focus
def jump_continuous(duration):
    dinput.keyDown("space")
    wait(duration)
    dinput.keyUp("space")

@require_focus
def reset_player(interval=0.5):
    dinput.press(("esc", "r", "enter"), interval=interval)

@require_focus
def leave_game(interval=0.5):
    dinput.press(("esc", "l", "enter"), interval=interval)

@require_focus
def toggle_shift_lock():
    dinput.press("shift")

@require_focus
def chat(message):
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