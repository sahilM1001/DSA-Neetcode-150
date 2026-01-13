# MEDIUM
# https://leetcode.com/problems/subsets/description/

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Input: nums = [0]
# Output: [[],[0]]

# Approach

class Solution:
    def subsets(self, nums):
        res = []
        curr = []
        def backtrack(index):
            if index >= len(nums):
                res.append(curr.copy())
                return 
            curr.append(nums[index])
            backtrack(index+1)
            
            curr.pop()
            backtrack(index+1)
        backtrack(0)
        return res
            