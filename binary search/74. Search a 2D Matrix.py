# MEDIUM
# https://leetcode.com/problems/search-a-2d-matrix/description/

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# Approach using Binary Search template
def searchMatrix(matrix, target):
    l = 0
    cols = len(matrix[0]) - 1
    rows = len(matrix)-1
    r = cols

    while l <= rows and r >= 0:
        if matrix[l][r] == target:
            return True
        elif matrix[l][r] >= target:
            r -= 1
        else:
            l += 1
            
    return False