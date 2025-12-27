# EASY
# https://leetcode.com/problems/single-number/description/

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Input: nums = [2,2,1]
# Output: 1

# Approach - Solved Using Bit Manipulation XOR Operation

# using 0 as starting point, XOR compares two elements, when both elements are same it returns 0 else returns the right side element as we are using 0 as starting

def singleNumber(nums):
        res = 0

        for i in nums:
            res = res ^ i
        return res

# Input: nums = [2, 2, 1]
# result = 0

# take 2:
#     result = 0 XOR 2 = 2

# take 2:
#     result = 2 XOR 2 = 0   // pair cancelled

# take 1:
#     result = 0 XOR 1 = 1

# return 1
