from game.players.player import Player


class Human(Player):
    """The human player
    
    The responsibility of Human is to act as the first player, controlled by a human

    """

    def __init__(self):
        """Constructs a new Human Player."""
        super().__init__()

