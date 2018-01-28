# -*- coding: utf-8 -*-
#Author:Maha Alidrisi

import random
import numpy as np
from prettytable import PrettyTable


class TicTactoe:
    

    def __init__(self, n):
        """create a board of X's and O's of given size n"""
        self.board = np.random.choice(a=['X', 'O'], size=(n, n))
    
    def scan_lines(self, lines):
        """returns the winner of the first occurance or no winner """
        for line in lines:
            if all(i == 'X' for i in line): 
                return 'The winner is: X'
            elif all(i == 'O' for i in line):
                return 'The winner is: O'
        return 'No winner'

    def get_the_winner(self):
        """returns the winner by scaning rows, columns, left and right digonal - in order - """
        winner = self.scan_lines(self.board) #sending the rows to scan_lines
        if winner == 'No winner':
            winner = self.scan_lines(self.board.T) #sending the columns to scan_lines
            if winner == 'No winner':
                winner = self.scan_lines([np.diagonal(self.board), np.diag(np.fliplr(self.board))]) #sending the left and right digonal to scan_lines
        return winner

    def __str__(self):
        """returns the board as a string"""
        pt = PrettyTable()
        for row in self.board:
            pt.add_row(row)
        return str(pt.get_string(header=False, border=False))

def main():
    t = TicTactoe(4)
    print(t)
    print('\n', t.get_the_winner(), '\n')

if __name__ == '__main__':
    main()
