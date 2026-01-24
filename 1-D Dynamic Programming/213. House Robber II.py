# MEDIUM
# https://leetcode.com/problems/house-robber-ii/description/

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.


# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Approach
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int: 
        if len(nums) == 1:
            return nums[0]
        # as it is a circular array, we can either loot from 0 to n-1
        # or we can loot 1 to n
        zero_to_n_1 = self.single_rob(nums[0:len(nums)-1]) # find max loot for 0 to n-1 case
        one_to_n = self.single_rob(nums[1:]) # find max loot for 1 to n case
        return max(one_to_n, zero_to_n_1) # return max between 0 to n-1 and 1 to n case
        
    def single_rob(self, nums: List[int]) -> int:
        # function to get max rob from a given list, based on the 198. House Robber Question
        if not nums: 
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1,len(nums)):
            #print(dp)
            if i- 1 > 0:
                dp[i] = nums[i] + max(dp[:i-1])
            else:
                dp[i] = nums[i]
        return max(dp)
        