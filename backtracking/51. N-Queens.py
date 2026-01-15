# HARD
# https://leetcode.com/problems/n-queens/description/

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Input: n = 4
# Output: [
#     [".Q..","...Q","Q...","..Q."],
#     ["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Input: n = 1
# Output: [["Q"]]
# Approach
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        boards = [] # init boards ans array
        board = [["."] * n for i in range(n)] # create board with . only

        cols = [False] * n # create cols lookup array of size n
        diag1 = [False] * (2*n-1) # create diagonal 1 lookup array of size 2*n-1
        diag2 = [False] * (2*n-1) # create diagonal 2 lookup array of size 2*n-1
        def backtrack(row):
            if row == n: # if we reach nth row we have found a valid solution, so we add it to boards and return to stop recursion
                boards.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                # run loop till n 
                if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                    # we can only place a queen when the col is not marked already, 
                    # and diagonal 1 at row + col index is not marked already
                    # and diagonal 2 at row - col + n - 1 is not marked already
                    board[row][col] = "Q" # we place the queen
                    cols[col] = True # Flip cols[col] to True
                    diag1[row + col] = True # Flip diagonal1[row + col] to True
                    diag2[row - col + n - 1] = True # Flip diagonal2 [row-col + n-1] to True

                    backtrack(row + 1) # move to next row

                    # backtrack and remove previously added queen and flags
                    board[row][col] = "."
                    cols[col] = False
                    diag1[row + col] = False
                    diag2[row - col + n - 1] = False

        backtrack(0) # start at row 0
        return boards