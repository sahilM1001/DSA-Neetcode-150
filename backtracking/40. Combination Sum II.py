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

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  
        res = []
        curr = []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break  

                curr.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                curr.pop()

        backtrack(0, target)
        return res