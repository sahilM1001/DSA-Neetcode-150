# MEDIUM
# https://leetcode.com/problems/surrounded-regions/description/

# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Approach
from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0]) # get total row cols in board
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # init directions
        vis = [[False] * COLS for _ in range(ROWS)] # init a visited grid

        arr = [] # empty array

        for c in range(COLS):
            # add all O from top and bottom rows to array and mark those index in the grid as visited
            # for top row
            if board[0][c] == "O":
                arr.append((0, c))
                vis[0][c] = True
            # for bottom row
            if board[ROWS-1][c] == "O":
                arr.append((ROWS - 1, c))
                vis[ROWS-1][c] = True
            
        for r in range(ROWS):
            # add all O from left and right columns and mark those as visited 
            # for left col
            if board[r][0] == "O":
                arr.append((r, 0))
                vis[r][0] = True
            # for right col
            if board[r][COLS-1] == "O":
                arr.append((r, COLS - 1))
                vis[r][COLS-1] = True
            
        # print(vis)
        def bfs(source, vis):
            q = deque(source) # init queue with source array
            while q:
                # while q is not empty pop an element from it
                r, c = q.popleft()
                # explore all four directions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # if new direction cell is not out of bounds, and its also not visited and it is O, 
                    # we mark it as visited, and append the new directions in the queue
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        not vis[nr][nc] and
                        board[nr][nc] == "O"
                    ):
                        q.append((nr, nc))
                        vis[nr][nc] = True
        bfs(arr, vis) # run bfs
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and not vis[i][j]:
                    # if item is O and its not visited change it to X
                    # if the item is O and not visited after bfs, 
                    # it means it cannot be connected to an O so it can be surrounded
                    board[i][j] = "X"
        