# MEDIUM
# https://leetcode.com/problems/subsets-ii/description/

# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Input: nums = [0]
# Output: [[],[0]]

# Approach
# goal is to find subsets without duplicates, so a similar approach to combination sum
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort() # sort input nums array
        res = [] # init ans array
        curr = [] # init curr ans array

        def backtrack(index):
            res.append(curr.copy()) # append current array to ans
                
            for i in range(index, len(nums)):
                # run loop starting at index to end of nums
                if i > index and nums[i] == nums[i - 1]:
                    # as nums are sorted, duplicate numbers will be together, so
                    # when i > index and current num in nums == prev num in nums
                    # keep the loop running 
                    continue

                curr.append(nums[i]) # if current num and prev num are different, append curr num to curr array
                backtrack(i+1) # explore recursion path for next num in the nums array
                curr.pop() # pop the last num 

        backtrack(0) # call backtracking function first time with 0 index
        return res
        