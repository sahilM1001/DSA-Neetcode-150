# MEDIUM
# https://leetcode.com/problems/subsets/description/

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Input: nums = [0]
# Output: [[],[0]]

# Approach
# goal here is to create a power set of the given set which includes all possible subsets. 

class Solution:
    def subsets(self, nums):
        res = [] # init ans array
        curr = [] # init current ans array
        def backtrack(index):
            if index >= len(nums): # when the index >= nums we append the ans and return to stop recursion
                res.append(curr.copy())
                return 
            curr.append(nums[index]) # pick num at current index and create all subsets based on that
            backtrack(index+1) # in combination with above line, this helps us find all subsets when we pick current number and next number in the list
            
            # next two lines explore all paths when we don't use current number and only take the next number
            curr.pop() # pop currently added number
            backtrack(index+1) # backtrack with next index num
        backtrack(0) # call backtracking function first time with 0 index
        return res
            