# -*- coding: utf-8 -*-
import unittest
from tictactoe import TicTactoe
import numpy as np


class TicTactoeTest(unittest.TestCase):

    
    def test_init(self):
        """test __init__ function"""
        t = TicTactoe(3)
        self.assertEqual(len(t.board), 3)
    
    def test_get_the_winner(self):
        """test get_the_winner function"""

        t2 = TicTactoe(3)
        #testcase: winner is a row seq, 2 winner, choose the first occurance
        t2.board = np.array([['X', 'X', 'O'], ['O', 'O', 'O'], ['X', 'X', 'X']]) 
        self.assertEqual(t2.get_the_winner(), 'The winner is: O') 
        #testcase: winner is a column seq, 2 winner, choose the first occurance
        t2.board = np.array([['X', 'X', 'O'], ['X', 'O', 'O'], ['X', 'X', 'O']]) 
        self.assertEqual(t2.get_the_winner(), 'The winner is: X') 
        #testcase: winner is a diagonal seq
        t2.board = np.array([['O', 'X', 'O'], ['X', 'O', 'X'], ['X', 'X', 'O']]) 
        self.assertEqual(t2.get_the_winner(), 'The winner is: O') 
        

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
