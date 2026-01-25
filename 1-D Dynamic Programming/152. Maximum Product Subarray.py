# MEDIUM
# https://leetcode.com/problems/maximum-product-subarray/description/

# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Approach
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # if len(nums) = 1 then max product will be the only array element 
        if len(nums) == 1:
            return nums[0]
        # init max sum with 1
        max_sum = 1
        res = max(nums) # init max product as max of nums
        min_sum = 1 # init min sum as 1 
        for i in range(0, len(nums)):
            # iterate over nums array
            temp = max_sum * nums[i] # calculate product as nums[i] * max_sum
            # set max_sum to max of temp or min_sum * nums[i] or nums[i], 
            # we use min_sum here as negative min sum * negative nums[i] can result into a positive bigger number
            max_sum = max(temp, min_sum * nums[i],nums[i]) 
            # set min sum to min of temp or min_sum * nums[i] or nums[i]
            min_sum = min(temp, min_sum * nums[i], nums[i])
            # update ans res to max of res, max_sum at every point
            res = max(res, max_sum)
        return res
        