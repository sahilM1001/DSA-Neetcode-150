# MEDIUM
# https://leetcode.com/problems/set-matrix-zeroes/description/

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
def setZeroes(matrix):
    row_set = set()
    col_set = set()
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if matrix[row][col] == 0:
                row_set.add(row)
                col_set.add(col)
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if row in row_set or col in col_set:
                matrix[row][col] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
# Output: [[1,0,1],[0,0,0],[1,0,1]]