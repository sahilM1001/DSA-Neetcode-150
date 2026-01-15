# MEDIUM
# https://leetcode.com/problems/combination-sum-ii/description/

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

# Approach
# goal here is to create combinations which reach a target, a single number cannot be used multiple times
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # sort candidate list
        res = [] #init ans array
        curr = [] # init current ans array

        def backtrack(start, remaining):
            if remaining == 0: 
                # if remaining/target becomes 0, we have reached a valid combination sum,
                # so append it to ans
                res.append(curr.copy())
                return

            for i in range(start, len(candidates)):
                # run a loop from start index passed to the function till end of candidates
                if i > start and candidates[i] == candidates[i - 1]:
                    # as candidates are sorted, duplicate numbers will be together, so
                    # when i > start and current num in candidates == prev num in candidates
                    # keep the loop running 
                    continue

                if candidates[i] > remaining:
                    # when current num in candidates > remaining, break the loop as exploring that path is unnecessary
                    break  

                curr.append(candidates[i]) # append current num in candidates
                backtrack(i + 1, remaining - candidates[i]) # call backtrack with new start position of i + 1 and new target becomes remaining - current num in candidates
                curr.pop() # pop it from curr

        backtrack(0, target) # call backtracking function first time with 0 index and target = target
        return res