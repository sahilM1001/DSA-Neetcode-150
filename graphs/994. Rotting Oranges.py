# MEDIUM
# https://leetcode.com/problems/rotting-oranges/description/

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# Approach

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque() # create new q
        rows = len(grid) # number of rows in grid
        cols = len(grid[0]) # number of cols in grid
        fresh = 0 # count of fresh oranges 
        mins = 0 # init minutes as 0
        
        # iterate over the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    # if it is a rotten orange, add to queue
                    q.append((r,c))
                if grid[r][c] == 1:
                    #if it is a fresh orange, increment fresh counter by 1
                    fresh +=1
        # if there are no fresh oranges, it means all oranges are either rotten or the grid is not valid, so we return 0 as ans
        if fresh == 0:
            return 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)] # four directions which can be explored from each grid cell
        while q:
            rotted = False # local flag init as False, it will be updated to true when an orange rots in current bfs layer
            for i in range(len(q)):
                # run till q size
                r,c = q.popleft() # get first rotten orange position from the q
                for dr, dc in directions:
                    # explore directions
                    nr = dr + r
                    nc = dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        # if the row and cols are inside bounds, and grid[current row][current col] is a fresh orange
                        grid[nr][nc] = 2 # mark it as rotten
                        fresh -=1 # decrease fresh orange count
                        q.append((nr, nc)) # append new row, new col as another rotten position to explore in the queue
                        rotted = True # update rotted to True so we can increase time in outer loop
            mins += 1 if rotted else 0 # add 1 to mins if an orange was rotten, else 0
        return mins if fresh ==0 else -1 # return mins if there were no fresh oranges at the end, else -1