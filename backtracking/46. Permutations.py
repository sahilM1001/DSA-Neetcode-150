# MEDIUM
# https://leetcode.com/problems/permutations/description/

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Input: nums = [1]
# Output: [[1]]

# Approach

class Solution:
    def permute(self, nums) :
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res


    def backtrack(self, perm, nums, pick):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False
        