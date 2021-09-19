import math 
import random

class Player:
    def __init__ (self, letter);
    # letter is for x or o
    self.letter = letter
    # for players to get their all moves

    def get_move(self, game):
        pass


    class RandomComPlayer(Player): # For computer player
        def __init__ (self , letter):
            super(),__init__(letter)
        
        def get_move(self, game):
            pass
    
    class HumanPlayer(Player): # For human player
        def __init__ (self, letter):
            super().__init__(letter)
        
        def get_move(self, game):
            pass
        