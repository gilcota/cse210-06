from game.players.player import Player
import random

class Computer(Player):
    """The computer player
    
    The responsibility of Computer is to act as a second player, controlled by the computer


    Attributes:
        _choice (str): The choice the computer takes
    """

    def __init__(self):
        """Constructs a new Computer Player."""
        super().__init__()
        self._choice = random.choice(("R","P","S"))

