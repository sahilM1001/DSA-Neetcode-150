# MEDIUM
# https://leetcode.com/problems/unique-paths/description/


# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.


# Input: m = 3, n = 7
# Output: 28

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# Approach

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        triangle = []
        num_rows = (m+n)-1

        for i in range(num_rows):
            current_row = [1]
            
            if i > 0:
                prev_row = triangle[-1]
                for j in range(1, i):
                    sum_above = prev_row[j - 1] + prev_row[j]
                    current_row.append(sum_above)
            if i > 0:
                current_row.append(1)
            
            triangle.append(current_row)
        return triangle[(m+n) - 2][m-1]


        