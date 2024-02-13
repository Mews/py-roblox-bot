
# pyrobloxbot

A python library to control the roblox character and interact with game ui through keyboard inputs

This library uses ```pydirectinput``` to control the keyboard and ensures that the roblox window is in focus to avoid unintentional consequences of sending keyboard inputs

## Installation

Install pyrobloxbot using ```pip install pyrobloxbot```

## Usage/Examples

```python
import pyrobloxbot as bot

#Send a message in chat
bot.chat("Hello world!")

#Walk forward for 5 seconds
bot.walk_forward(5)

#Reset player character
bot.reset_player()
```
## Documentation

[Read the full documentation](https://linktodocumentation)

