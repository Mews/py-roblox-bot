# Changelog
### 1.0.9
-   Added docs for the module's global variables

-   Added `launch_game` function to open a roblox game from its id

    Example:

    ```python
    import pyrobloxbot as bot

    id = 2753915549 # The game id for Blox Fruits
    bot.launch_game(id)
    ```

-   Added `press_key` and `hold_key` aliases for `keyboard_action` and `hold_keyboard_action` functions respectively

-   Added `ui_scroll_up` and `ui_scroll_down` functions to scroll through ui elements

-   Added `key_up` and `key_down` functions to hold and release keys without blocking execution

-   Fixed issue with using `leave_game` function while ui navigation is enabled

-   Added `image_is_visible` function to check wheter a given image is present on screen

    Example:
    ```python
    import pyrobloxbot as bot
    from time import sleep

    #Wait until the button.png image is visible before continuing
    #The function only has to be 80% confident about whether the image is visible to continue
    #This is still almost guaranteed to not give false positives

    while not bot.image_is_visible("button.png", confidence=0.8):
        sleep(0.5) #Wait a bit before checking again
    
    print("The button is on screen!")
    ```
    
### 1.0.8
This version was missing some dependencies

Other than that, the changes present in 1.0.9 also apply to this version, even though using it isn't recommended

### 1.0.7
-   Added failsafe that can be triggered by key combination (default is control + m)

    The failsafe hotkey can be changed through `set_failsafe_hotkey`

    Example:
    ```python
    #Sets the failsafe hotkey to control + shift + y
    set_failsafe_hotkey("ctrl", "shift", "y")
    ```

-   The key used to toggle the ui navigation mode can now be changed by changing the `UI_NAV_KEY` variable

    Example:
    ```python
    import pyrobloxbot as bot
    bot.UI_NAV_KEY = "~" # The tilde key will now be used to turn on the ui navigation mode
    ```

-   Added `ui_navigate` function which takes a direction string and calls the corresponding ui navigation function

    `ui_navigate` raises `InvalidUiDirectionException` if the direction argument is not in `literals.UI_NAVIGATE_DIRECTIONS.VALUES` 

-   `walk` function can now take multiple walk directions as arguments at the same time to walk diagonally

### 1.0.6
-   `require_focus` decorator no longer runs when importing module

-   `keyboard_action` and `hold_keyboard_action` can now take multiple keys as arguments at the same time

    Example:

    ```python
    #Hold "a", "b" and "c" at the same time for 2 seconds
    hold_keyboard_action("a", "b", "c", duration=2)
    ```

### 1.0.5
Added docstrings

### 1.0.4
First stable release