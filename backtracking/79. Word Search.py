# MEDIUM
# https://leetcode.com/problems/word-search/description/

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Input: board = [
#             ["A","B","C","E"],
#             ["S","F","C","S"],
#             ["A","D","E","E"]
#         ], 
# word = "ABCCED"
# Output: true

# Input: board = [
#         ["A","B","C","E"],
#         ["S","F","C","S"],
#         ["A","D","E","E"]
#     ],
# word = "SEE"
# Output: true

# Approach

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board) # m rows in board
        cols = len(board[0]) #n cols in board
        visited = [[False] * cols for i in range(rows)] # init visited map for each cell in board
        def backtrack(row, col, word_index):
            if word_index == len(word): # if word index == len(word to find), we have a match so return True
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols:
                # if we are out of bounds at either row or cols, we return False as we have exhausted search space
                return False
            if visited[row][col]:
                # if the current cell is already visited, prune this path as there is no need to explore this further
                return False
            if board[row][col] != word[word_index]:
                # if current char on board != char at word_index in word to search, prune this path 
                return False
            visited[row][col] = True # mark cell visited as true
            found = (
                backtrack(row - 1, col, word_index + 1) or # explore in previous row (up)
                backtrack(row + 1, col, word_index + 1) or # explore in next row (down)
                backtrack(row, col - 1, word_index + 1) or # explore in previous column (left)
                backtrack(row, col + 1, word_index + 1) # explore in next column (right)
            )

            visited[row][col] = False # backtrack and make the cell unvisited

            return found # return value of Found, either true or false
            
        # run the backtracking for every i,j combination to search word presence in the board
        for i in range(rows):
            for j in range(cols):
                if backtrack(i,j, 0):
                    return True

        return False