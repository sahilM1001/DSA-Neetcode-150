# MEDIUM
# https://leetcode.com/problems/spiral-matrix/description/


# Given an m x n matrix, return all elements of the matrix in spiral order.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Approach

# We want to traverse a matrix in spiral order:
# right → down → left → up, repeatedly, moving inward layer by layer.

# A clean iterative way to do this is to maintain four boundaries:

# top → the topmost unvisited row
# bottom → one past the bottommost unvisited row
# left → the leftmost unvisited column
# right → one past the rightmost unvisited column
# At each step, we walk along the current outer boundary in four directions:

# left → right across the top row
# top → bottom down the right column
# right → left across the bottom row
# bottom → top up the left column
# After each pass, we shrink the boundaries inward.

def spiralOrder(matrix):
    res = []
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    
    while left < right and top < bottom:
        for i in range(left, right):
            res.append(matrix[top][i])
        top+=1
        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -=1
        if not (left < right and top < bottom):
            break
        for i in range(right-1, left-1, -1):
            res.append(matrix[bottom-1][i])
        bottom -= 1
        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left+=1
    return res