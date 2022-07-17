
class Player():
    """The different actors of the game
    
    The responsibility of Player is to represent the parties involved in the game


    Attributes:
        _score (int): Tracks player's score
        _choice (str): Defines a player's choice 
    """

    def __init__(self):
        """Constructs a new Player."""
        self._score = 0
        self._choice = ""

    def get_score(self):
        """Gets the score of the player
        
        Returns:
            _score (int): The score of the player
        """
        return self._score

    def get_choice(self):
        """Gets the choice of the player
        
        Returns:
            _choice (str): The choice of the player
        """
        return self._choice

    def set_score(self, score):
        """Updates the score to the given one.
        
        Args:
            _score (int): The given score.
        """
        self._score = score

    def set_choice(self, choice):
        """Updates the choice to the given one.
        
        Args:
            _choice (str): The given choice.
        """
        self._choice = choice