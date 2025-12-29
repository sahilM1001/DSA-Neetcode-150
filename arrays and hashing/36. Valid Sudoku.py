# MEDIUM
# https://leetcode.com/problems/valid-sudoku/description/

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Approach 
# For every valid board[i][j] we will check if it is already present in row[i][num] or col[j][num] or box[block_pos][num], 
# if that is the case our sudoku is invalid, else we keep marking the row[i][num], col[j][num] and box[block_pos][num] as true 
# the num here will be calculated as ord(board[i][j] - ord('1'))
# the block_pos will be calculated as block_pos = (i//3) * 3 + (j//3)

def isValidSudoku(board):
    rows = [[False] * 9 for _ in range(9)]
    cols = [[False] * 9 for _ in range(9)]
    boxes = [[False] * 9 for _ in range(9)]

    for i in range(0, 9):
        for j in range(0, 9):
            cur_ele = board[i][j]
            block_pos = (i//3) * 3 + (j//3)
            num = ord(board[i][j]) - ord('1')
            if cur_ele == ".":
                continue
            if rows[i][num] or cols[j][num] or boxes[block_pos][num]:
                return False
            rows[i][num] = True
            cols[j][num] = True
            boxes[block_pos][num] = True
    return True