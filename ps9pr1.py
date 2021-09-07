#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 20:59:32 2019

@author: diegomurcia
"""

class Board:
    def  __init__(self, height, width):
        """ constructs a new Board object with an attribute height
            that stores the number of rows in the board, an attribute
            width that stores the number of columns in the board, and
            an attribute slots that stores a reference to a two-dimensional
            list with height rows and width columns that will be used to store 
            the current contents of the board.
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

    # Add code here for the hyphens at the bottom of the board
    # and the numbers underneath it.
        s += '-'
        for c in range(self.width):
            s += '--'
        s += '\n'
        s += ' '
        for line in range(self.width):
            s += str(line % 10) + ' '

        return s
    
    def add_checker(self, checker, col):
        """ adds a checker in column col
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        # put the rest of the method here
        r = 0
        while r <= self.height:
            if self.slots[self.height - r - 1][col] == ' ':
                self.slots[self.height - r - 1][col] = checker
                break
            else:
                r += 1
                
    def reset(self):
        """ resets the board
        """
        for r in range(self.height):
            for c in range(self.width):
                if self.slots[self.height - r - 1][c] != ' ':
                    self.slots[self.height - r - 1][c] = ' ' 
        
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
        
    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the 
            column col on the calling Board object. Otherwise, it 
            should return False. 
        """
        if col >= self.width:
            return False
        elif col < 0:
            return False
        else:
            for r in range(self.height):
                if self.slots[r][col] == ' ':
                    return True
                else:
                    return False
    def is_full(self):
        """returns True if the called Board object is completely 
           full of checkers, and returns False otherwise.
        """
        for r in range(self.height):
            for c in range(self.width):
                if self.slots[r][c] == ' ':
                    return False
                else:
                    return True
    def remove_checker(self, col):
        """ removes top checker in column col
        """
        for r in range(self.height):
                if self.slots[r][col] != ' ':
                    self.slots[r][col] = ' '
                    break
        
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                       return True

    # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker):
        """Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                       return True
        return False
    
    def is_up_diagonal_win(self,checker):
        """Checks for a upward diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 3][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 1][col + 3] == checker:
                       return True
        return False
    
    def is_down_diagonal_win(self,checker):
        """ Checks for a downward diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                       return True
        return False
        
    def is_win_for(self, checker):
        """Checks for a win for the specified checker.
        """
        if self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True:
               return True
        else:
            return False
           
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        