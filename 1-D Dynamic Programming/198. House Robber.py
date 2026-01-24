# MEDIUM
# https://leetcode.com/problems/house-robber/description/

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# Approach
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        dp = [0] * len(nums) # init dp array of length same as input num
        dp[0] = nums[0] # dp[0] = nums[0]

        for i in range(1,len(nums)):
            #print(dp)
            if i- 1 > 0:
                # max possible loot is current house stash + max until now
                dp[i] = nums[i] + max(dp[:i-1])
            else:
                dp[i] = nums[i]
        return max(dp) # return max from dp array
        