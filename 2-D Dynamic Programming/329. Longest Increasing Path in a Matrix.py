# HARD
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].

# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

# Input: matrix = [[1]]
# Output: 1

# Approach
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {} # create dp memo dict
        max_rows = len(matrix) # get max rows in matrix
        max_cols = len(matrix[0]) # get max cols in matrix

        def dfs(r,c):
            if (r,c) in memo:
                # if r, c is already explored and in memo, return value 
                return memo[(r,c)]
            # res was init as 1 as the current path should be atleast of length 1 because of the current cell
            res, a1,a2,a3,a4 = 1, 0, 0, 0, 0
            # explore previous row if val at matrix[prev_row][col] > matrix[current_row][col]
            # previous row should be >= 0 and < max_rows and col >=0 and < max_cols
            if 0 <= r-1 < max_rows and 0 <= c < max_cols and matrix[r-1][c] > matrix[r][c]:
                a1 = dfs(r-1,c)

            # explore next row if val at matrix[next_row][col] > matrix[current_row][col]
            # next row should be >= 0 and < max_rows and col >=0 and < max_cols
            if 0 <= r+1 < max_rows and 0 <= c < max_cols and matrix[r+1][c] > matrix[r][c]:
                a2 = dfs(r+1,c)
            
            # explore previous col if val at matrix[row][prev_col] > matrix[row][prev_col]
            # row should be >= 0 and < max_rows and col-1 >=0 and < max_cols
            if 0 <= r < max_rows and 0 <= c-1 < max_cols and matrix[r][c-1] > matrix[r][c]:
                a3 = dfs(r,c-1)

            # explore next col if val at matrix[row][next_col] > matrix[row][next_col]
            # row should be >= 0 and < max_rows and col+1 >=0 and < max_cols
            if 0 <= r < max_rows and 0 <= c+1 < max_cols and matrix[r][c+1] > matrix[r][c]:
                a4 = dfs(r,c+1)
            # update res to res + max(path length from previous row, path length from next row, path length from previous col, path length from next col)
            res = res + max(a1,a2,a3,a4)
            memo[(r,c)] = res # update memo
            return res # return res
        ans_max = float('-inf')
        for i in range(max_rows):
            for j in range(max_cols):
                # for every row, col starting point, get the max increasing path length and update ans
                ans_max = max(ans_max, dfs(i,j))
        return ans_max # return final ans
        