from __future__ import annotations
from functools import wraps
from time import sleep as wait
import pydirectinput as dinput
from pygetwindow import getWindowsWithTitle, getActiveWindow
from win32gui import GetWindowText, GetForegroundWindow
import pyperclip as pyclip
from .exceptions import *
from .literals import KEYBOARD_KEYS, WALK_DIRECTIONS

UI_NAV_ENABLED = False

def require_focus(fn):
    """A decorator that ensures the roblox window is in focus before running the decorated function. This is used by all pyrobloxbot functions

    :raises NoRobloxWindowException: Raised when can't find a roblox window to focus
    """
    #Fast check to see if roblox window is already focused
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if GetWindowText(GetForegroundWindow()) == "Roblox":
            return fn(*args, **kwargs)

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

            return fn(*args, **kwargs)        

    return wrapper

@require_focus
def keyboard_action(action:KEYBOARD_KEYS.VALUES):
    """Presses a keyboard key

    :param action: The key to be pressed
    :type action: KEYBOARD_KEYS
    """
    dinput.press(action)

@require_focus
def hold_keyboard_action(action:KEYBOARD_KEYS.VALUES, duration:float):
    """Holds a keyboard key for a given time

    :param action: The key to be held
    :type action: KEYBOARD_KEYS
    :param duration: How long to hold for, in seconds
    :type duration: float
    """
    dinput.keyDown(action)
    wait(duration)
    dinput.keyUp(action)

def walk(direction:WALK_DIRECTIONS.VALUES, duration:float):
    """Walks in a direction for a given time

    :param direction: The direction to walk in
    :type direction: WALK_DIRECTIONS
    :param duration: How long to walk for, in seconds
    :type duration: float
    :raises InvalidWalkDirectionException: Raised when given direction isn't in literals.WALK_DIRECTIONS.VALUES
    """
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
    """Walks forward for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    dinput.keyDown("w")
    wait(duration)
    dinput.keyUp("w")

@require_focus
def walk_left(duration:float):
    """Walks left for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    dinput.keyDown("a")
    wait(duration)
    dinput.keyUp("a")

@require_focus
def walk_right(duration:float):
    """Walks right for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    dinput.keyDown("d")
    wait(duration)
    dinput.keyUp("d")

@require_focus
def walk_back(duration:float):
    """Walks back for a given time

    :param duration: How long to walk for, in seconds
    :type duration: float
    """
    dinput.keyDown("s")
    wait(duration)
    dinput.keyUp("s")

@require_focus
def jump(number_of_jumps:int=1, delay:float=0):
    """Jumps for a given number of times

    :param number_of_jumps: How many times to jump, defaults to 1
    :type number_of_jumps: int
    :param delay: How much time between jumps, in seconds, defaults to 0
    :type delay: float
    """
    for i in range(number_of_jumps):
        dinput.press("space")
        wait(delay)

@require_focus
def jump_continuous(duration:float):
    """Holds jump for a given time

    :param duration: How long to hold jump for, in seconds
    :type duration: float
    """
    dinput.keyDown("space")
    wait(duration)
    dinput.keyUp("space")

@require_focus
def reset_player(interval:float=0.5):
    """Resets player character

    :param interval: How long between each keyboard input, in seconds, defaults to 0.5
    :type interval: float
    """
    dinput.press(("esc", "r", "enter"), interval=interval)

@require_focus
def leave_game(interval:float=0.5):
    """Leaves the current game

    :param interval: How long between each keyboard input, in seconds, defaults to 0.5
    :type interval: float
    """
    dinput.press(("esc", "l", "enter"), interval=interval)

@require_focus
def toggle_shift_lock():
    """Toggles shift lock (Shift lock switch must be enabled in roblox settings)
    """
    dinput.press("shift")

@require_focus
def chat(message:str):
    """Sends a message in chat

    :param message: The message to send
    :type message: str
    """
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
    """Toggles ui navigation mode. This is called by all ui navigation functions if ui navigation mode is disabled
    """
    global UI_NAV_ENABLED
    UI_NAV_ENABLED = not UI_NAV_ENABLED
    dinput.press('`')

@require_focus
def ui_navigate_up():
    """Navigate up in ui elements
    """
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press('up')

@require_focus
def ui_navigate_left():
    """Navigate left in ui elements
    """
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press('left')

@require_focus
def ui_navigate_right():
    """Navigate right in ui elements
    """
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press('right')

@require_focus
def ui_navigate_down():
    """Navigate down in ui elements
    """
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press('down')

@require_focus
def ui_click():
    """Click on currently selected ui element
    """
    if not UI_NAV_ENABLED:
        toggle_ui_navigation()

    dinput.press("enter")

@require_focus
def equip_slot(slot:int):
    """Equip a given item slot

    :param slot: The item slot to equip
    :type slot: int
    :raises InvalidSlotNumberException: Raised when slot isn't between 0 and 9
    """
    if slot < 0 or slot > 9:
        raise InvalidSlotNumberException("Slots should be between 0 and 9")

    dinput.press(str(slot))