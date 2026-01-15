# MEDIUM
# https://leetcode.com/problems/combination-sum/description/

# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
    
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Approach
# goal here is to create combinations which reach a target, a single number can be used multiple times

class Solution:
    def combinationSum(self, candidates, target):
        res = [] # init ans array
        curr = [] # init current ans array
        def backtrack(index):
            if sum(curr) == target: # if current sum == target, append current array to ans and stop recursion
                res.append(curr.copy())
                return 
            if sum(curr) > target: # if sum(curr) > target, stop recursion as this path is not good to explore
                return
            if index == len(candidates): # if we reach end of candidates arr return and stop recursion
                return
            if sum(curr) + candidates[index] <= target:
                # if sum(curr) + candidates[index] <= target, this is a valid path to explore
                # so we append it to current array and go deeper to explore it
                curr.append(candidates[index])
                backtrack(index)
                # finally pop the current number from current array 
                curr.pop()
            # explore recursion path for not picking current number 
            backtrack(index+1)
        backtrack(0) # call backtracking function first time with 0 index
        return res
        