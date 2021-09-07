#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:
    
    def __init__(self, checker):
        """constructs a new Player object by initializing the following two 
           attributes
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """ returns a string representing a Player object.
        """
        s = ''
        s += 'Player ' + str(self.checker)
        return s
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker of the 
            Player object’s opponent.
        """
        if self.checker == 'X':
            return 'O'
        if self.checker =='O':
            return 'X'
    def next_move(self, b):
        """accepts a Board object b as a parameter and returns the column 
           where the player wants to make the next move.
        """
        self.num_moves += 1
        while True:
            move = input('Enter a column: ')
            if move in '0123456':
                col = int(move)
                if b.can_add_to(col) == True:
                    return col
            print ('Try Again!')
                
































































