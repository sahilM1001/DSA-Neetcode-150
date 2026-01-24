# EASY
# https://leetcode.com/problems/climbing-stairs/description/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Approach

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        steps = [-1]*(n+1) # init steps array till n+1 steps
        steps[0] = 0 # step 0 can be reached in 0 way
        steps[1] = 1 # step 1 can be reached in 1 way
        steps[2] = 2 # step 2 can be reached in 2 ways 1+1, or 2 
        for i in range(3, n+1):
            # from n = 3, every step can be reached in total of n-1 + n-2 ways 
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n] # return steps[n]