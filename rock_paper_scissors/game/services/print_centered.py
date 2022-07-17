import shutil

class PrintCentered:
    """A service that centers text in the terminal.
    
    The responsibility of PrintCentered is to show a text outputs centedered int eh terminal.
    """
    
    def print_centered(self, phrase):
        """Centers the received text to be shown on the terminal"""
        print(phrase.center(shutil.get_terminal_size().columns)) 

