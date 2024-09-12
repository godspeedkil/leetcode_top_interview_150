"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
"""
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            current_row = set()
            current_column = set()
            current_box = set()
            for j in range(9):
                next_box = board[(3*(i//3)) + (j//3)][(j%3) + (3*(i%3))]
                if board[i][j] in current_column:
                    return False
                elif board[i][j] != '.':
                    current_column.add(board[i][j])
                if board[j][i] in current_row:
                    return False
                elif board[j][i] != '.':
                    current_row.add(board[j][i])
                if next_box in current_box:
                    return False
                elif next_box != '.':
                    current_box.add(next_box)
        return True