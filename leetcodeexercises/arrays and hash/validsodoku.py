import collections


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #first create rows, cols and squares to store values
        #ensure that only 1 of each no 1-9 occurs

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if (board[i][j] == '.'):
                    continue
                #lol forgot to account for . so everything just returned false
                if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i//3,j//3)]):
                    # divide by 3 so u can get the corr row and col for the square it is in
                    # the key is a tupple
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])
        return True
""" key learning point:
basically use collections to decide default stored value of dictionaries
and tuples can also be used as keys for dictionaries
"""


