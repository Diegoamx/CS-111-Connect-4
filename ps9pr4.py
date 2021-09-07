#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        self.checker = checker
        self.tiebreak = tiebreak
        self.lookahead = lookahead     
        super().__init__(checker)
    
    def __repr__(self):
        """returns a string representing an AIPlayer object.
        """
        s = ''
        s += 'Player ' + str(self.checker) + ' (' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
        return s
        
    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the board,
           and that returns the index of the column with the maximum score.
        """
        mscore = []
        for x in range(len(scores)):
            if scores[x] == max(scores):
                mscore.append(x)
        if self.tiebreak == 'LEFT':
            return mscore[0]
        elif self.tiebreak == 'RIGHT':
            return mscore[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(mscore)
        
    def scores_for(self, b):
       scores = [50] * b.width
       for col in range(b.width):
           if b.can_add_to(col) == False:
               scores[col] = -1
           elif b.is_win_for(Player(self.checker).opponent_checker()):
               scores[col] = 0
           elif b.is_win_for(self.checker):
               scores[col] = 100
           elif self.lookahead == 0:
               scores[col] = 50
           else:
               b.add_checker(self.checker, col)
               opp = AIPlayer(Player(self.checker).opponent_checker(), self.tiebreak,(self.lookahead - 1))
               opp_score = opp.scores_for(b)
               if opp_score[col] == 0:
                   scores[col] = 100
               elif opp_score[col] == 100:
                   scores[col] = 0
               else:
                   scores[col] = 50
               b.remove_checker(col)
       return scores
    
    def next_move(self, board):
        """overrides the next_move method from Player, returns the calledAIPlayer's judgement of its best possible move, a column number
        """
        self.num_moves = 0
        for col in range(board.width): 
            if AIPlayer.max_score_column == False:
                self.num_moves += 1
        return self.num_moves

    
    
    
    
    
    
    
    
    
    
    
            
                