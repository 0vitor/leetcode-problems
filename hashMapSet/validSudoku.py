from collections import defaultdict
from typing import Counter


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        c = set()
        for row in board:
            for n in row:
                if n in c:
                    return False
                elif n != '.':
                    c.add(n)
            c.clear()

        c.clear()

        for column in zip(*board):
            for n in column:
                if n in c:
                    return False
                elif n != '.':
                    c.add(n)
            c.clear()

        c.clear()
        j = 0
        i = 0
        for _ in range(3):
            for _ in range(3):
                for _ in range(len(board)):
                    n = board[i][j]
                    if n in c:
                        return False
                    elif n != '.':
                        c.add(n)
                    j += 1
                    if j % 3 == 0:
                        j -= 3
                        i += 1
                c.clear()

                j += 3
                i -= 3
            j = 0
            i += 3

        return True

class Solution2(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
                    print(res)
        return len(res) == len(set(res))

board = [
 ["5","3","5",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(Solution2().isValidSudoku(board))
