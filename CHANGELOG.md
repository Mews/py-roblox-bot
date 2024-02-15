# Changelog
### 1.0.4
First stable release

### 1.0.5
Added docstrings

### 1.0.6
-   `require_focus` decorator no longer runs when importing module

-   `keyboard_action` and `hold_keyboard_action` can now take multiple keys as arguments at the same time

    Example:

    ```python
    #Hold "a", "b" and "c" at the same time for 2 seconds
    hold_keyboard_action("a", "b", "c", duration=2)
    ```

### 1.0.7
-   Added failsafe that can be triggered by key combination (default is control + m)

    The failsafe hotkey can be changed through `set_failsafe_hotkey`

-   The key used to toggle the ui navigation mode can now be changed by changing the `UI_NAV_KEY` variable

    Example:
    ```python
    import pyrobloxbot as bot
    bot.UI_NAV_KEY = "~" # The tilde key will now be used to turn on the ui navigation mode
    ```

-   Added `ui_navigate` function which takes a direction string and calls the corresponding ui navigation function

    `ui_navigate` raises `InvalidUiDirectionException` if the direction argument is not in `literals.UI_NAVIGATE_DIRECTIONS.VALUES` 

-   `walk` function can now take multiple walk directions as arguments at the same time to walk diagonally