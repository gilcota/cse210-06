from game.players.player import Player

class Protagonist(Player):
    """The protagonist of the game, it means, rock, paper and scissors
    
    The responsibility of Player is to represent the parties involved in the game


    Attributes:
        _rock (list): ASCII representation of a rock
        _rock_x_2 (list): ASCII representation of both player's rock
        # _paper (list): ASCII representation of a paper
        _paper_x_2 (list): ASCII representation of both player's paper
        _scissors (list): ASCII representation of scissors
        _scissors_x_2 (list): ASCII representation of both player's scissors
        _rock_paper_scissors (list): ASCII representation of rock, paper and scissors.
    """

    def __init__(self):
        """Constructs a new Protagonist."""
        super().__init__()
        # rock
        self._rock = [
            "    _______  ",
            "---'   ____) ",
            "      (_____)",
            "      (_____)",
            "      (____) ",
            "---.__(___)  ",
            "",    
            "      Rock   ",     
            "",
        ]
        # both player's Rock
        self._rock_x_2 = [
            "       _______        _______    ",
            "   ---'   ____)      (____   '---",
            "         (_____)    (_____)      ",
            "         (_____)    (_____)      ",
            "         (____)      (____)      ", 
            "   ---.__(___)        (___)__.---", 
            "",
            "                Rock             ",
            "",
        ]

        # paper
        self._paper = [
            "    _______     ",
            "---'   ____)__  ",
            "        ______) ", 
            "        _______)",  
            "       _______)",
            "---.________)  ",
            "",
            "      Paper     ",
            "",
        ]

        # both player's paper
        self._paper_x_2 = [
            "    ____                  ____    ",
            "---'____)____        ____(____'---",
            "       ______)      (______       ",
            "       _______)    (_______       ",
            "      _______)      (_______      ",
            "---._______)          (_______.---",
            "",
            "               Paper              ",
            "",
        ]

        # scissors
        self._scissors = [
            "    _______       ",
            "---'   ____)____  ",
            "          ______) ", 
            "       __________)",  
            "      (____)      ",
            "---.__(___)       ",
            "",
            "     Scissors     ",
            "",
        ]

        # both player's scissors
        self._scissors_x_2 = [
            "    _______                  _______    ",
            "---'   ____)____        ____(____   '---",
            "          ______)      (______          ",
            "       __________)    (__________       ",
            "      (____)                (____)      ",
            "---.__(___)                  (___)__.---",
            "",
            "                 Scissors               ",
            "",
        ]
        
        # rock, paper and scissors together 
        self._rock_paper_scissors = [
            "    _______             ____                  _______       ",
            "---'   ____)        ---'____)____         ---'   ____)____  ",
            "      (_____)              ______)                  ______) ", 
            "      (_____)              _______)              __________)",  
            "      (____)              _______)              (____)      ",
            "---.__(___)         ---._______)          ---.__(___)       ",
            "",
            "       R                    P                       S       ",
            "",
        ]