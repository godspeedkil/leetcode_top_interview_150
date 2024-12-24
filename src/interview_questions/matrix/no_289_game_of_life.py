"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
"""
from copy import deepcopy

class Solution:
    def __get_next_cell_state(self, board, row, col) -> int:
        curr_val = board[row][col]
        m = len(board)
        n = len(board[0])
        neighbors = [0] * 2
        neighbors[curr_val] -= 1
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i >= 0 and i < m and j >= 0 and j < n:
                    neighbors[board[i][j]] += 1
        if neighbors[1] == 3:
            return 1
        elif neighbors[1] > 3:
            return 0
        elif neighbors[1] < 2:
            return 0
        elif curr_val == 1 and neighbors[1] == 2:
            return 1
        else:
            return 0

    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        copy = deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                next_state = self.__get_next_cell_state(copy, i, j)
                board[i][j] = next_state