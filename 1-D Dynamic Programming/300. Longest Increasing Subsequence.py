# MEDIUM
# https://leetcode.com/problems/longest-increasing-subsequence/description/

# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

# Approach
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # create dp array with 1 of len nums
        dp = [1] * len(nums)
        max_len = float('-inf') # init max_len 
        for i in range(1, len(nums)):
            # start loop for 1 to n nums
            for j in range(0, i):
                # run another loop till i
                if nums[j] < nums[i]:
                    # if num at j < num at i 
                    # update dp[i] with max between dp[i] or dp[j] + 1
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) # return max of dp
        