# EASY
# https://leetcode.com/problems/missing-number/

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Input: nums = [3,0,1]
# Output: 2
# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Approach 1 using maths: 
# sum of n natural numbers - sum of provided array will return missing number
def missingNumber(nums):
    return int((len(nums) * (len(nums) + 1)) / 2 - sum(nums))

# Approach 2 Using Bit Manipulation:
# Let’s restate what your logic is doing in words:
# Start with x = n
# → because n exists in the full range 0..n, but does not exist in nums
# For every index i:

# XOR i into x

# XOR nums[i] into x

# Everything that appears twice cancels
# The only number that appears once is the missing number
# That’s exactly the required reasoning.

def missingNumber(nums):
    x = len(nums)
    for i in range(0, len(nums)):
        x = x ^ i # x XOR i will reset to 0 if x and i are same 
        x = x ^ nums[i] # x XOR nums[i] will reset to 0 if x and nums[i] are same
    return x # x will be the missing number at the end