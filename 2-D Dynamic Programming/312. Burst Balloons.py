# HARD
# https://leetcode.com/problems/burst-balloons/description/

# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

# Return the maximum coins you can collect by bursting the balloons wisely.

# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

# Input: nums = [1,5]
# Output: 10
 

# Approach
from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1] # add 1 to starting and ending of nums as discussed in question
        n = len(nums) # get len of nums array
        memo = {} # create dp memo dict

        def dp(l,r):
            if r-l == 1:
                # if r - l == 1 return 0
                return 0
            if (l,r) in memo:
                # if l,r in memo return memo
                return memo[(l,r)]
            ans = 0 # init ans as 0
            for k in range(l+1, r):
                # run loop from l+1 to r
                # coins at curr index will be dp(l,k) + nums[l] * nums[k] * nums[r] + dp(k,r) 
                coins = dp(l, k) + nums[l] * nums[k] * nums[r] + dp(k,r)
                ans = max(ans, coins) # update ans
            memo[(l,r)] = ans # update memo with ans
            return ans # return ans
        return dp(0, n-1) # start at left 0 and r n-1