class NoRobloxWindowException(Exception):
    """Raised when a function can't find a roblox window to focus
    """
    pass

class InvalidSlotNumberException(Exception):
    """Raised by equip_slot when slot isn't between 0 and 9
    """
    pass

class InvalidWalkDirectionException(Exception):
    """Raised by walk when given a direction that isn't in literals.WALK_DIRECTIONS.VALUES
    """
    pass