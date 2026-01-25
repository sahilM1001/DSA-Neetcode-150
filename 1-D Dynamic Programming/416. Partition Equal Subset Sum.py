# MEDIUM
# https://leetcode.com/problems/partition-equal-subset-sum/description/

# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

# Approach
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 !=0:
            # if the sum of nums is not even, we cannot create equal length partitions of the nums array 
            # so return false
            return False
        # the target sum for one partition is sum of nums // 2
        target = sum(nums)//2
        dp = [False] * (target + 1) # create a dp array of length target + 1 with false
        dp[0] = True # mark 0 as true

        for num in nums:
            # for each number in nums
            for j in range(len(dp)-1,-1,-1):
                # iterate the dp array in reverse
                # if dp[current] is true and j + num < target + 1 , it means dp[j + num] should also be true. 
                if dp[j] and j + num < target + 1:
                    dp[j+num] = True
        return dp[target] #return dp target
        