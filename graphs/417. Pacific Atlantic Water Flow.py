# MEDIUM
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

# Approach
from typing import List
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0]) # get grid rows, cols
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # init four directions
        pac = [[False] * COLS for _ in range(ROWS)] # pacific grid
        atl = [[False] * COLS for _ in range(ROWS)] # atlantic grid

        pacific = [] # pacific array
        atlantic = [] # atlantic array
        for c in range(COLS):
            pacific.append((0, c)) # add top row
            atlantic.append((ROWS - 1, c)) # add bottom row

        for r in range(ROWS):
            pacific.append((r, 0)) # add first col for each row
            atlantic.append((r, COLS - 1)) # add last col for each row
        
        def bfs(source, ocean):
            q = deque(source) # init queue with passed source array
            while q:
                # while items in q, pop items and mark that cell as visited
                r, c = q.popleft()
                ocean[r][c] = True
                # explore all four directions for the cell
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # if the new direction cell is not out of bounds, and it is not already visited, 
                    # and its height is greater than existing current cell at r,c add it to queue 
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))
                        
        bfs(pacific, pac) # run bfs for pacific ocean
        bfs(atlantic, atl) # run bfs for atlantic ocean

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]: 
                    # when pacific[row][col] is visited and atlantic[row][col] is visited
                    # add to answer arr
                    res.append([r, c])
        return res
