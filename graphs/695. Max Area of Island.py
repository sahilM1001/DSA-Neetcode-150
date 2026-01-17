# MEDIUM
# https://leetcode.com/problems/max-area-of-island/description/

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

# Approach

from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid) # total rows in grid
        m = len(grid[0]) # total cols in grid
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # 4 directions that can be access from any grid location
        area = 0

        def bfs(r, c):
            q = deque() # init empty queue
            grid[r][c] = 0 # mark current as island so it is not explored again
            q.append((r,c)) # add current row, col to queue
            res = 1 # init area as 1
            while q:
                # run loop till q is not empty
                row, col = q.popleft() # pop from queue
                for dr, dc in directions: # explore the four directions
                    nr = dr + row # new row direction
                    nc = dc + col # new col direction
                    if nr < 0 or nr >= n or nc < 0 or nc >= m or grid[nr][nc] == 0:
                        # if there are any water continue or row or col are out of bounds continue, 
                        continue
                    # else add it to the queue 
                    q.append((nr, nc))
                    grid[nr][nc] = 0 # mark current as 0 to ensure it is not visited again
                    res += 1 # increase area
            return res # return area

        # iterate over original grid and whenever we encounter an island,
        # run a bfs for that i,j position and get the area
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = max(area, bfs(i, j))
        return area
        