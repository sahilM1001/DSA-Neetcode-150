# MEDIUM
# https://leetcode.com/problems/subsets-ii/description/

# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Input: nums = [0]
# Output: [[],[0]]

# Approach

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()  
        res = []
        curr = []

        def backtrack(index):
            res.append(curr.copy())
                
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue

                curr.append(nums[i])
                backtrack(i+1)
                curr.pop()

        backtrack(0)
        return res
        