import time
import random
import os
from game.services.print_centered import PrintCentered
from game.players.protagonist import Protagonist
from game.players.human import Human
from game.players.computer import Computer

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _service (PrintCentered): Commands to print centered in the terminal
        _protagonist (Protagonist): Rock, paper and scissors art
        _human (Human): The human player of the game
        _computer (Computer): The computer player of the game
        replay (boolean): Whether or not to play again
        human_choice (str): Records the human player choice
        computer_choice (str): Defines a computer's player random choice 
        human_score (int): Tracks human player score
        computer_score (int): Tracks computer player score      
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._service = PrintCentered()
        self._protagonist = Protagonist()
        self._human = Human()
        self._computer = Computer()
        self.replay = "Y"
        self.human_choice = ""
        self.computer_choice = ""
        self.human_score = 0
        self.computer_score = 0
        clear = lambda: os.system('cls')



    def start_game(self):
        """Starts the game and runs the game loop.
        """
        self.game_welcome()
        
        #loop to continue playing
        while self.replay == "Y":
            self.game_action()
            self.game_playing()
            self.game_results()

    def game_welcome(self):
        """Shows introductory mesagge to the game
        """

        # Welcome rock
        clear = lambda: os.system('cls')        
        clear()
        self._service.print_centered("Welcome to")

        time.sleep(1)

        for i in self._protagonist._rock:
            self._service.print_centered(i)

        time.sleep(1)

        # Welcome paper
        clear = lambda: os.system('cls')        
        clear()
        self._service.print_centered("Welcome to")

        for i in self._protagonist._paper:
            self._service.print_centered(i)

        time.sleep(1)

        # Welcome scissors
        clear = lambda: os.system('cls')        
        clear()
        self._service.print_centered("Welcome to")

        for i in self._protagonist._scissors:
            self._service.print_centered(i)

        time.sleep(2)

    def game_action(self):
        """Records the selection action from both the human and computer player
        """

        # shows all options to choose
        clear = lambda: os.system('cls')                
        clear()
        for i in self._protagonist._rock_paper_scissors:
            self._service.print_centered(i)

        # human chooses option and records it
        self.human_choice = input("Choose your destiny (R, P, S): ")
        
        self._human.set_choice(self.human_choice)

        # computer generates random option nad records it
        self.computer_choice = random.choice(("R","P","S"))

        self._computer.set_choice(self.computer_choice)

    def game_playing(self):
        """Shows the playing sequence
        """
        # start the duel!!
        clear = lambda: os.system('cls')
        clear()
        print("\n\n\n\n")
        self._service.print_centered("Let the duel begin!!!")

        time.sleep(2)

        # show rocks shaking
        clear = lambda: os.system('cls')        
        clear()
        for i in self._protagonist._rock_x_2:
            self._service.print_centered(i)

        time.sleep(1)

        # show papers shaking
        clear = lambda: os.system('cls')        
        clear()
        for i in self._protagonist._paper_x_2:
            self._service.print_centered(i)

        time.sleep(1)

        # show scissors shaking
        clear = lambda: os.system('cls')        
        clear()
        for i in self._protagonist._scissors_x_2:
            self._service.print_centered(i)

        time.sleep(1)
    
    def game_results(self):
        """Shows game results: winner, losser and points
        """
        # shows human's player choice
        clear = lambda: os.system('cls')
        clear()
        self._service.print_centered("You chose: ")

        # depending on the selection, the image
        if self._human.get_choice() == "R":
            for i in self._protagonist._rock:
                self._service.print_centered(i)
        elif self._human.get_choice() == "P":
            for i in self._protagonist._paper:
                self._service.print_centered(i)
        else:
            for i in self._protagonist._scissors:
                self._service.print_centered(i)

        time.sleep(2)

        # shows computer's player choice
        print("\n\n")
        self._service.print_centered("I chose: ")

        # depending on the selection, the image
        if self._computer.get_choice() == "R":
            for i in self._protagonist._rock:
                self._service.print_centered(i)
        elif self._computer.get_choice() == "P":
            for i in self._protagonist._paper:
                self._service.print_centered(i)
        else:
            for i in self._protagonist._scissors:
                self._service.print_centered(i)

        time.sleep(2)

        
        print("\n\n")

        # shows who is the winner, with a corresponding message
        # draw
        if (self._human.get_choice() == "R" and self._computer.get_choice() == "R") or (self._human.get_choice() == "P" and self._computer.get_choice() == "P") or (self._human.get_choice() == "S" and self._computer.get_choice() == "S"):
            self._service.print_centered("It is a draw, what a drama!!!")
        # human player winner
        elif (self._human.get_choice() == "R" and self._computer.get_choice() == "S") or (self._human.get_choice() == "P" and self._computer.get_choice() == "R") or (self._human.get_choice() == "S" and self._computer.get_choice() == "P"):
            self._service.print_centered("You got me, you are the winner!!!")
            self.human_score += 1
            self._human.set_score(self.human_score)
        # human player looser
        else:
            self._service.print_centered("Sorry kid, try again\n")
            time.sleep(1)
            self._service.print_centered("You are a looser!!!")
            self.computer_score += 1
            self._computer.set_score(self.computer_score)

        time.sleep(2)

        # shows score
        print(f"\n\n\nYour score = {self._human.get_score()}")
        print(f"My score = {self._computer.get_score()}")
        
        # play again check
        self.replay = input("\nWanna play again (Y, N)? ")


