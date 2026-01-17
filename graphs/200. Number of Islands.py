# MEDIUM
# https://leetcode.com/problems/number-of-islands/description/

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# Appraoach
from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid) # total rows in grid
        m = len(grid[0]) # total cols in grid
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # up down left right directions
        vis = [[False] * m for _ in range(n)] # grid visited cell
        count = 0 # count for island

        def bfs(r, c):
            q = deque() # init empty queue
            grid[r][c] = "0" # mark current as island so it is not explored again
            q.append((r,c)) # add current row, col to queue
            while q:
                row, col = q.popleft() # pop from queue
                for dr, dc in directions: 
                    # find in all directions, 
                    nr = dr + row
                    nc = dc + col
                    if nr < 0 or nr >= n or nc < 0 or nc >= m or grid[nr][nc] == "0":
                        # if there are any water continue or row or col are out of bounds continue, 
                         
                        continue
                    # else add it to the queue 
                    q.append((nr, nc)) 
                    grid[nr][nc] = "0" # mark grid[newrow][newcol] as water so it is not revisited

        # iterate over original grid and whenever we encounter an island,
        # increase count of island and run bfs
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count+=1
                    bfs(i, j)
        return count